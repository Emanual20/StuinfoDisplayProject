<template>
  <div class="manageinfo">
    <Header />

    <div class="container">
      <div class="card-body">
          this is manage info space..
      </div>
    </div>
 
    <Footer />
  </div>


</template>

<script>
import Header from "../components/HeaderComp.vue";
import Footer from "../components/FooterComp.vue";
import { GetInfoPost } from "../apis/read.js";
import { CheckPwPost } from "../apis/read.js";
import { ref, reactive, onMounted } from "@vue/composition-api";
import { useStore } from 'vuex';
import Axios from "axios";
import router from "../router";
import store from "../store";

export default {
  name: "ManageInfoView",
  components: {
    Header,
    Footer
  },
  setup(props, context){
    const store = useStore();
    let username = ref('');
    let password = ref('');
    error_message = ref('');
    onMounted(()=>{
      console.log(context.root.$route.path)
    });

    return{
      username, 
      password, 
      error_message,
    }
  },

  data(){
    return{
      text: 'hello world to check test() function',
      retCode: -1,
    }
  },

  methods:{
    test(){
      const testParams = reactive({
        url: 'checknamepw', 
        key: 'namepw',
        username: username.value,
        password: password.value,
      });
      CheckPwPost(testParams).then(resp=>{
        this.text = resp.data.message;
        this.retCode = resp.data.data[0];
        store.dispatch("UpdateUserStateAction", {
          username: username.value,
          password: password.value,
          is_login: true,
        });
        router.push({name: 'Stuinfo'});
      })
      .catch(err=>{
        this.text = 'error' + err;
        let error_message = "please check your username and password again..";
        alert(error_message);
      })
    },
  }

};
</script>