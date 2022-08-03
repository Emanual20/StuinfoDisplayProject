<template>
    <b-container id="header">
      <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand href="/">InfoSpace</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <ul  class="navbar-nav ml-auto" v-if="!$store.state.user.is_login">
            <a class="nav-link" href="/login/">登录</a>
          </ul>
          <ul  class="navbar-nav ml-auto" v-else>
            <a class="nav-link"> {{ $store.state.user.username }} </a>
            <button @click="checkinfo()" class="btn position-relative">
              查看信息
            </button>
            <button @click="manageinfo()" class="btn position-relative">
              个人信息更新
            </button>
            <button @click="manageperm()" class="btn position-relative">
              权限管理
            </button>            
            <a class="nav-link" @click="logout()"> 退出登录 </a>
            <!-- <a class="nav-link" href="/"> 退出登录 </a> -->
          </ul>
        </b-collapse>
      </b-navbar>
    </b-container>
</template>

<script>
import { ref } from "@vue/composition-api";  // ref 定义常量; reactive：定义对象
import { store } from "../store";
import { router } from "../router" ;
import { useStore } from 'vuex';
// import { use } from "vue/types/umd.js";

export default {
    name: "Header",
    setup(props, context){
      const now_url = ref(context.root.$route.path);
      return {
        now_url,
      };
    },
    methods:{
      checkinfo(){
        this.$router.push({name: 'Stuinfo'});
      },
      manageinfo(){
        this.$router.push({name: 'Manageinfo'});
      },
      manageperm(){
        this.$router.push({name: "Manageperm"});
      },
      logout(){
        console.log("Log out begin..!");
        this.$store.dispatch("LogoutAction",{
        });
        console.log("Log out finish..!");
        this.$router.push({name: 'Home'});
      }
    }
}
</script>

<style lang="scss" scoped>
@media (max-width:500px) {
  #Header{
    margin-top:90px
  }
}
</style>