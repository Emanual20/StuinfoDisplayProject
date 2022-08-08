<template>
  <div class="login">
    <Header />

    <div class="container">
      <div class="card-body">
        <!-- If you wanna make register function available, change blockedregister() into tryregister() method -->
        <form @submit.prevent="blockedregister()">
        <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label">Email address</label>
            <input v-model="emailaddress" type="email" class="form-control" id="emailaddress" aria-describedby="emailHelp">
            <div id="emailHelp" class="form-text"><b>The email address will be set as your login username.</b></div>
        </div>
        <div class="mb-3">
            <label for="exampleInputNickname1" class="form-label">Nickname</label>
            <input v-model="username" type="text" class="form-control" id="username" aria-describedby="NicknameHelp">
            <div id="NicknameHelp" class="form-text"><b>The email address will be set as your login username.</b></div>
        </div>
        <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label">Password</label>
            <input v-model="password" type="password" class="form-control" id="password"> 
            <div id="PasswordHelp" class="form-text"><b>Default Password is your real ID number which with exactly 18 characters. The Password shall pass automatically security check.</b></div><br>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="exampleCheck1">
            <label class="form-check-label" for="exampleCheck1">我同意将我的信息用于网站建设。</label>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
        </form>

      </div>
    </div>
 
    <Footer />
  </div>


</template>

<script>
import Header from "../components/HeaderComp.vue";
import Footer from "../components/FooterComp.vue";
import { RegisterUserPost } from "../apis/update.js";
import { ref, reactive, onMounted } from "@vue/composition-api";
import { useStore } from 'vuex';
import Axios from "axios";
import router from "../router";
import store from "../store";


export default {
  name: "LoginView",
  components: {
    Header,
    Footer
  },
  setup(props, context){
    let emailaddress = ref('');
    let username = ref('');
    let password = ref('');
    let error_message = ref('');
    onMounted(()=>{
      console.log(context.root.$route.path)
    });

    return{
      emailaddress,
      username, 
      password, 
      error_message,
    }
  },

  data(){
    return{
      text: 'some log',
      retCode: -1,
    }
  },

  methods:{
    blockedregister(){
      let text = "Register service is not available for users now.";
      console.log(text);
      alert(text);
    },
    tryregister(){
      console.log("In Register View:", "email:", emailaddress.value,"username:", username.value, "\npassword:", password.value);
      const testParams = reactive({
        url: 'registernewuser', 
        key: 'register',
        emailaddress: emailaddress.value,
        username: username.value,
        password: password.value,
      });
      RegisterUserPost(testParams).then(resp=>{
        this.text = resp.data.message;
        alert(this.text);
        router.push({name: 'LoginView'});
      })
      .catch(err=>{
        this.text = 'error' + err.message;
        let error_message = "Internal server error or this email already exists..";
        alert(error_message);
      })
    },
  }

};
</script>