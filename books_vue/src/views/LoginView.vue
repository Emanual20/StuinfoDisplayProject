<template>
  <div class="login">
    <Header />

    <div class="container">
      <div class="card-body">
        <form @submit.prevent="test()">
          <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label">Username</label>
            <input
              v-model="username"
              type="text"
              class="form-control"
              id="username"
              aria-describedby="emailHelp"
            />
            <div id="emailHelp" class="form-text">
              <b
                >Default username is your real name in Chinese.
                如：杨希，王航。</b
              >
            </div>
          </div>
          <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label"
              >Password</label
            >
            <input
              v-model="password"
              type="text"
              class="form-control"
              id="password"
            />
            <div id="emailHelp" class="form-text">
              <b
                >Default Password is your real ID number which with exactly 18
                characters. 如：12010420040804181X。</b
              >
            </div>
          </div>
          <!-- <div class="error-message"> {{ error_message }} </div> -->
          <button type="submit" class="btn btn-primary">Login</button>
        </form>
      </div>
    </div>

    <Footer />
  </div>
</template>

<script>
import Header from "../components/HeaderComp.vue";
import Footer from "../components/FooterComp.vue";
import { CheckPwPost } from "../apis/read.js";
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
    onMounted(() => {
      console.log(context.root.$route.path);
    });

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
          router.push({ name: "Selfinfo" });
        })
        .catch(err => {
          this.text = "error" + err;
          let error_message = "please check your username and password again..";
          alert(error_message);
        });
    }
  }
};
</script>
