<template>
  <div id="ChangepwdView">
    <Header />
    <b-container>
      <div class="container">
        <div class="card-body">
          <h4><b>修改密码</b></h4>
          <br />
          <form @submit.prevent="trychangepwd()">
            <div class="mb-3">
              <label for="exampleInputPassword1" class="form-label"
                >新密码</label
              >
              <input
                v-model="password"
                type="password"
                class="form-control"
                id="password"
              />
              <div id="PasswordHelp" class="form-text">
                <b>新密码将代替原密码用于登录。</b>
              </div>
            </div>
            <div class="mb-3">
              <label for="exampleInputPassword2" class="form-label"
                >确认新密码</label
              >
              <input
                v-model="password_confirm"
                type="password"
                class="form-control"
                id="password_confirm"
              />
              <div id="PasswordHelp" class="form-text">
                <b>请再输入一次新密码。</b>
              </div>
              <br />
            </div>
            <button type="submit" class="btn btn-primary">确认</button>
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
  name: "ChangepwdView",
  components: {
    Header,
    Footer
  },
  setup(props, context) {
    let password = "";
    let password_confirm = "";
    let error_message = "";
    onMounted(() => {
      console.log(context.root.$route.path);
    });
    return {
      password,
      password_confirm,
      error_message
    };
  },
  methods: {
    trychangepwd() {
      const testParams = reactive({
        url: "updatepassword",
        key: "updatepassword",
        username: this.$store.state.user.username,
        npassword: password.value
      });
      if (password.value != password_confirm.value) {
        alert("password and password_confirm not equal!");
        return {};
      }
      console.log("try to update password");
      UpdatePasswordPost(testParams)
        .then(resp => {
          alert("Update finish..");
          this.$store.dispatch("LogoutAction", {});
          this.$router.push({ name: "LoginView" });
        })
        .catch(err => {
        });
    }
  }
};
</script>

<style lang="scss" scoped></style>
