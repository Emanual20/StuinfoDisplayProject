<template>
  <div class="login">
    <Header />

    <div class="container">
      <div class="card-body">
        <!-- If you wanna make register function available, change blockedregister() into tryregister() method -->
        <form @submit.prevent="tryregister()">
          <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label"
              >邮箱 (i.e. 用户名)</label
            >
            <input
              v-model="emailaddress"
              type="email"
              class="form-control"
              id="emailaddress"
              aria-describedby="emailHelp"
            />
            <div id="emailHelp" class="form-text">
              <b>用于保证您提供的邮箱只对应一个线上用户，并作为用于登录该系统的用户名。</b>
            </div>
          </div>

          <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label"
              >密码</label
            >
            <input
              v-model="password"
              type="password"
              class="form-control"
              id="password"
            />
            <div id="PasswordHelp" class="form-text">
              <b>您给出的密码需要通过自动的安全检查，将作为用于登录该系统的密码。</b>
            </div>
            <br />
          </div>

          <div class="mb-3">
            <label for="exampleInputNickname1" class="form-label"
              >姓名</label
            >
            <input
              v-model="username"
              type="text"
              class="form-control"
              id="username"
              aria-describedby="UsernameHelp"
            />
            <div id="UsernameHelp" class="form-text">
              <b>只供展示信息使用。</b>
            </div>
          </div>

          <div class="mb-3">
            <label for="highbatch" class="form-label"
              >高中入学年份</label
            >
            <input
              v-model="highbatch"
              type="text"
              class="form-control"
              id="highbatch"
              aria-describedby="HighbatchHelp"
            />
            <div id="HighbatchHelp" class="form-text">
              <b>如您是2015年高中入学，2018年毕业，则为2015级。请在文本框内输入2015。</b>
            </div>
          </div>

          <div class="mb-3">
            <label for="highclass" class="form-label"
              >高中所在班级</label
            >
            <input
              v-model="highclass"
              type="text"
              class="form-control"
              id="highclass"
              aria-describedby="HighclassHelp"
            />
            <div id="HighclassHelp" class="form-text">
              <b>如您是2015级2班。请在文本框内输入2。</b>
            </div>
          </div>

          <div class="mb-3">
            <label for="hightutor" class="form-label"
              >高中（第一任）班主任</label
            >
            <input
              v-model="hightutor"
              type="text"
              class="form-control"
              id="hightutor"
              aria-describedby="HightutorHelp"
            />
            <div id="HightutorHelp" class="form-text">
              <b>注册验证问题，作为验证您为真实的用户的唯一凭据。请填写您高中班主任姓名的全拼，如南开的全拼是nankai。</b>
            </div>
          </div>

          <button type="submit" class="btn btn-primary">注册</button>
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
    let emailaddress = "";
    let password = "";
    let username = "";
    let highbatch = "";
    let highclass = "";
    let hightutor = "";

    let error_message = "";
    onMounted(() => {
      console.log(context.root.$route.path);
    });

    return {
      emailaddress,
      username,
      password,
      highbatch,
      highclass,
      hightutor,
      error_message
    };
  },

  data() {
    return {
      text: "some log",
      retCode: -1
    };
  },

  methods: {
    blockedregister() {
      let text = "Register service is not available for users now.";
      alert(text);
    },
    tryregister() {
      const testParams = reactive({
        url: "registernewuser",
        key: "register",
        emailaddress: emailaddress.value,
        username: username.value,
        password: password.value,
        highbatch: highbatch.value,
        highclass: highclass.value,
        hightutor: hightutor.value
      });
      RegisterUserPost(testParams)
        .then(resp => {
          alert("Register Successful");
          router.push({ name: "LoginView" });
        })
        .catch(err => {
        });
    }
  }
};
</script>
