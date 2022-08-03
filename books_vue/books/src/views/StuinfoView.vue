<template>
  <div class="stuinfo">
    <Header />

    <div class="container">
      <div class="card-body">
        This is info page. Please <b> Press Button </b> to Access Data: 
        <button type="button" class="btn btn-success" @click="test()"> Button </button>
      </div>
      <table class="table table-striped table-hover">
        <thead>
          <tr>
            <th scope="col">Name</th>
            <th scope="col">City</th>
            <th scope="col">Dest</th>
            <th scope="col">Major</th>
            <th scope="col">MasterorPhd</th>
            <th scope="col">Period</th>
            <th scope="col">Infos</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="niter1 in $store.state.nlist.nlist1" :key="niter1.id">
            <th scope="col"> {{niter1.stu_touuid}} </th>
            <th scope="col"> {{niter1.stu_city}} </th>
            <th scope="col"> {{niter1.stu_dest}} </th>
            <th scope="col"> {{niter1.stu_mastermajor}} </th>
            <th scope="col"> {{niter1.stu_masterorphd}} </th>
            <th scope="col"> {{niter1.stu_masterperiod}} </th>
            <th scope="col"> {{niter1.further_info}} </th>
          </tr>
          <tr v-for="niter2 in $store.state.nlist.nlist2" :key="niter2.id">
            <th scope="col"> {{niter2.stu_touuid}} </th>
            <th scope="col"> {{niter2.stu_city}} </th>
            <th scope="col"> {{niter2.stu_dest}} </th>
            <th scope="col"> {{niter2.stu_mastermajor}} </th>
            <th scope="col"> {{niter2.stu_masterorphd}} </th>
            <th scope="col"> {{niter2.stu_masterperiod}} </th>
            <th scope="col"> {{niter2.further_info}} </th>
          </tr>
        </tbody>
      </table>
    </div>
 
    <Footer />
  </div>


</template>

<script>
import Header from "../components/HeaderComp.vue";
import Footer from "../components/FooterComp.vue";
import { FetchAdmittedInfoPost, GetInfoPost } from "../apis/read.js";
import { CheckPwPost } from "../apis/read.js";
import { ref, reactive, onMounted } from "@vue/composition-api";
import { Store, useStore } from 'vuex';
import Axios from "axios";
import router from "../router";
import store from "../store";


export default {
  name: "StuinfoView",
  components: {
    Header,
    Footer
  },
  setup(props, context){
    let nlist1 = [];
    let nlist2 = [];

    onMounted(()=>{
      console.log(context.root.$route.path)
    });

    return{
      username, 
      password, 
      nlist1,
      nlist2,
    }
  },

  data(){
    return{
      text: 'hello world to check test() function',
      nlist1: [],
      nlist2: [],
    }
  },

  methods:{
    test(){
      const FetchInfoParams = reactive({
          url: 'fetchadmittedinfo',
          key: 'fetchinfo',
          username: store.state.user.username,
      });
      FetchAdmittedInfoPost(FetchInfoParams).then(resp => {
        this.text = resp.data.message;
        this.nlist1 = resp.data.data[0];
        this.nlist2 = resp.data.data[1];
        console.log(this.nlist1);
        this.$store.dispatch("UpdateNlistAction", {
          nlist1: this.nlist1,
          nlist2: this.nlist2,
        });
      })
      .catch(err => {
        this.text = 'error' + err;
        alert(this.text);
      })
    },
  }

};
</script>