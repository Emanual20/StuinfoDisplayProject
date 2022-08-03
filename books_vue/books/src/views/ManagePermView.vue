<template>
  <div class="managepoerm">
    <Header />

    <div class="container">
      <div class="card-body">
        <div class="permissioninfo">
        <h4><b> 权限管理: </b></h4>
        若您想一键修改<b>所有同学</b>对您详细个人信息可查看权限，请使用下述选项。<br>

        <div class="form-check form-switch">
          <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckChecked" checked>
          <label class="form-check-label" for="flexSwitchCheckChecked">允许所有同学查看详细信息</label>
        </div>

        <br>若您想单独修改<b>某个同学</b>对您详细个人信息的查看权限，请使用下述选项。<br>
        <div v-for="niter in studentData.students" :key="niter.id">
          <div class="form-check form-switch">
            <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckChecked" checked>
            <label class="form-check-label" for="flexSwitchCheckChecked">允许同学{{niter['stu_name']}}: 查看详细信息</label>
          </div>
        </div>

        </div>
      </div>
    </div>
 
    <Footer />
  </div>


</template>

<script>
import Header from "../components/HeaderComp.vue";
import Footer from "../components/FooterComp.vue";
import { GetStudents } from "../apis/read.js";
import { ref, reactive, onMounted } from "@vue/composition-api";
import { useStore } from 'vuex';
import Axios from "axios";
import router from "../router";
import store from "../store";

export default {
  name: "ManagePermView",
  components: {
    Header,
    Footer
  },
  setup(props, context){
    let username = ref('');
    let password = ref('');
    let error_message = ref('');
    
    const studentData = reactive({
      students: []
    })

    onMounted(()=>{
      console.log(context.root.$route.path)
    });

    GetStudents().then(response => {
      console.log(studentData.students);
      studentData.students = response.data.data;
      console.log(studentData.students);
    });

    return{
      username, 
      password, 
      studentData,
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

    },
  }

};
</script>