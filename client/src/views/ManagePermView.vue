<template>
  <div class="managepoerm">
    <Header />

    <div class="container">
      <div class="card-body">
        <div class="permissioninfo">
          <h4><b> 权限管理</b></h4>
          <div class="p-4 mb-4">
            您想让所有<b>同班同学</b>匿名（不匿名）查看您的本科后相关去向，默认匿名。
            <b>非同班同学不可见任何信息。</b>
          </div>
          
          <div class="p-3 mb-3">
              <button
                  type="button"
                  @click.prevent="UpdateSelfPermission(1)"
                  class="btn btn-success float-left"
                >
                  不匿名
              </button>
              <button
                type="button"
                @click.prevent="UpdateSelfPermission(0)"
                class="btn btn-danger float-right"
              >
                匿名
              </button>
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
import { UpdatePermPost } from "../apis/update.js";
import { ref, reactive, onMounted } from "@vue/composition-api";
import Axios from "axios";
import router from "../router";
import store from "../store";

export default {
  name: "ManagePermView",
  components: {
    Header,
    Footer
  },
  setup(props, context) {
    let error_message = "";

    const allpermData = reactive({
      permvalue: 0
    });

    return {
      allpermData,
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
    UpdateSelfPermission(tp) {
      const testParams = reactive({
        url: "updateselfpermission",
        username: this.$store.state.user.username,
        stu_uuid: this.$store.state.user.uuid,
        tp: tp
      });
      UpdatePermPost(testParams)
        .then(resp => {
          alert("Success..!");
        })
        .catch(err => {
        });
    },
  }
};
</script>
