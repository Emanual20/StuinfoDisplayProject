<template>
  <b-container id="header">
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand href="/">NK-Stuinfo</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <ul class="navbar-nav ml-auto" v-if="!$store.state.user.is_login">
          <a class="nav-link" href="/login/">登录</a>
          <a class="nav-link" href="/register/">注册</a>
        </ul>
        <ul class="navbar-nav ml-auto" v-else>
          <a class="nav-link" @click="checkselfinfo()">
            {{ $store.state.user.username }}
          </a>
          <!-- <a class="nav-link" @click="changepassword()"> 修改密码 </a> -->
          <a class="nav-link" @click="manageinfo()"> 更新信息 </a>
          <a class="nav-link" @click="checkstuinfo()"> 我的班级 </a>
          <a class="nav-link" @click="checkmapinfo()"> 地图预览 </a>
          <a class="nav-link" @click="manageperm()"> 权限管理 </a>
          <a class="nav-link" @click="checkspitslot()"> 匿名吐槽 </a>
          <a class="nav-link" @click="logout()"> 退出登录 </a>
        </ul>
      </b-collapse>
    </b-navbar>
  </b-container>
</template>

<script>
import { ref } from "@vue/composition-api"; // ref 定义常量; reactive：定义对象
import { store } from "../store";
import { router } from "../router";
import { useStore } from "vuex";
// import { use } from "vue/types/umd.js";

export default {
  name: "Header",
  setup(props, context) {
    return {
      
    };
  },
  methods: {
    checkspitslot() {
      this.$router.push({ name: "Spitslot" });
    },
    checkselfinfo() {
      this.$router.push({ name: "Selfinfo" });
    },
    changepassword() {
      this.$router.push({ name: "Changepwd" });
    },
    checkstuinfo() {
      this.$router.push({ name: "Stuinfo" });
    },
    checkmapinfo(){
      this.$router.push({ name: "Mapinfo" });
    },
    manageinfo() {
      this.$router.push({ name: "Manageinfo" });
    },
    manageperm() {
      this.$router.push({ name: "Manageperm" });
    },
    logout() {
      console.log("Log out begin..!");
      this.$store.dispatch("LogoutAction", {});
      console.log("Log out finish..!");
      this.$router.push({ name: "Home" });
    }
  }
};
</script>

<style lang="scss" scoped>
@media (max-width: 500px) {
  #Header {
    margin-top: 90px;
  }
}
</style>
