<template>
<div id="Selfinfo">
    <Header />
    <b-container class="mt-4 mb-2">
        <div class="container">
        <div class="card-body">
            <h5><b>修改密码：</b></h5>
            <form @submit.prevent="trychangepwd()">
            <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label">新密码</label>
                <input v-model="password" type="password" class="form-control" id="password"> 
                <div id="PasswordHelp" class="form-text"><b>新密码将代替原密码用于登录。</b></div><br>
            </div>
            <div class="mb-3">
                <label for="exampleInputPassword2" class="form-label">确认新密码</label>
                <input v-model="password_confirm" type="password" class="form-control" id="password_confirm"> 
                <div id="PasswordHelp" class="form-text"><b>请再输入一次新密码。</b></div><br>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
            </form>

        </div>
        </div>

    </b-container>
    <Footer />
</div>
</template>

<script>
import Header from "../components/HeaderComp.vue";
import Footer from "../components/FooterComp.vue";
import { UpdatePasswordPost } from "../apis/update.js";
import { ref, reactive, onMounted } from "@vue/composition-api";
import Axios from "axios";
import router from "../router";
import store from "../store";

export default {
    name:"SelfinfoView",
    components:{
        Header,
        Footer,
    },
    setup(props, context){
        let password = ref('');
        let password_confirm = ref('');
        let error_message = ref('');
        onMounted(()=>{
        console.log(context.root.$route.path)
        });
        return{
            password,
            password_confirm,
            error_message,
        }
    },
    methods:{
        trychangepwd(){
        const testParams = reactive({
            url: 'updatepassword', 
            key: 'updatepassword',
            username: this.$store.state.user.username,
            npassword: password.value,
        });
        if(password.value != password_confirm.value){
            alert('password and password_confirm not equal!');
            return {};
        }
        console.log("try to update password");
        UpdatePasswordPost(testParams).then(resp=>{
            this.text = resp.data.message;
            alert(this.text);
            this.$store.dispatch("LogoutAction", {});
            this.$router.push({name: "LoginView"});
        })
        .catch(err=>{
            this.text = 'error' + err.message;
            let error_message = "Internal server error..";
            alert(error_message);
        })
        },
    }
}
</script>

<style lang="scss" scoped>

</style>