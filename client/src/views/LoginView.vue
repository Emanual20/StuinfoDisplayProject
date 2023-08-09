<template>
  <div class="login">
    <Header />

    <div class="container">
      <div class="card-body">
        <form @submit.prevent="test()">
          <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label">用户名</label>
            <input
              v-model="username"
              type="text"
              class="form-control"
              id="username"
              aria-describedby="emailHelp"
            />
            <div id="emailHelp" class="form-text">
              <b
                >默认用户名为您的真实中文姓名。如：杨希。</b
              >
            </div>
          </div>
          <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label"
              >密码</label
            >
            <input
              v-model="password"
              type="text"
              class="form-control"
              id="password"
            />
            <div id="emailHelp" class="form-text">
              <b
                >如忘记密码或其他事项，请联系<a href="mailto:emanual20@foxmail.com">网站管理员</a>。</b
              >
            </div>
          </div>
          <button type="submit" class="btn btn-primary">登录</button>
        </form>
      </div>
    </div>

    <Footer />
  </div>
</template>

<script>
import Header from "../components/HeaderComp.vue";
import Footer from "../components/FooterComp.vue";
import { CheckPwPost, FetchMapInfo } from "../apis/read.js";
import { ref, reactive, onMounted } from "@vue/composition-api";
import { useStore } from "vuex";
import Axios from "axios";
import router from "../router";
import store from "../store";

export default {
  name: "LoginView",
  components: {
    Header,
    Footer
  },
  setup(props, context) {
    let username = "";
    let password = "";
    let error_message = "";

    return {
      username,
      password,
      error_message
    };
  },

  data() {
    return {
      text: "hello world to check test() function",
      retCode: -1
    };
  },

  methods: {
    test() {
      console.log("username:", username.value, "\npassword:", password.value);
      const testParams = reactive({
        url: "checknamepw",
        key: "namepw",
        username: username.value,
        password: password.value
      });
      CheckPwPost(testParams)
        .then(resp => {
          this.text = resp.data.message;
          this.$store.dispatch("UpdateUserStateAction", {
            username: username.value,
            password: password.value,
            uuid: resp.data.data[0]["stu_uuid"],
            is_login: true
          });

          const FetchInfoParams = reactive({
            url: "fetchmapinfo",
            key: "fetchinfo",
            username: store.state.user.username
          });
          FetchMapInfo(FetchInfoParams)
          .then(resp => {
            store.dispatch("UpdateNmapAction", {
              nmap: resp.data.data[0],
            });
          })
          .catch(err => {
            this.text = "error" + err;
            alert(this.text);
          });
          router.push({ name: "Selfinfo" });
        })
        .catch(err => {
        });
    }
  }
};
</script>
