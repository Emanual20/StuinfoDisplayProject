<template>
  <div class="SelfinfoView">
    <Header />

    <div class="container">
      <div class="card-body">
        <div class="personalinfo">
          <h4><b>个人信息 </b></h4>
          <br />

          <div v-if="stu_permission.permission_type !== 3">
            <b>由于你是管理员，因此你没有信息需要展出。</b>
          </div>
          <div v-else>
            <div class="bachelorgroup">
              <label for="basic-url" class="form-label"
                ><b>本科相关信息</b></label
              >
              <br />

              <form class="row g-3">
                <div class="col-md-4">
                  <label for="text" class="form-label"
                    >本科学校：{{ bachelor_info.bachelor_school }}
                  </label>
                </div>
                <div class="col-md-4">
                  <label for="inputCity" class="form-label"
                    >本科城市：{{ bachelor_info.bachelor_city }}
                  </label>
                </div>
                <div class="col-md-4">
                  <label for="inputCity" class="form-label"> </label>
                </div>
                <div class="col-md-4">
                  <label for="text" class="form-label"
                    >本科专业：{{ bachelor_info.bachelor_major }}
                  </label>
                </div>
                <div class="col-md-4">
                  <label for="text" class="form-label"
                    >本科转入专业：{{ bachelor_info.bachelor_major_trans }}
                  </label>
                </div>
                <div class="col-md-4">
                  <label for="text" class="form-label"
                    >本科二专业（双学位、辅修）：{{
                      bachelor_info.bachelor_major_second
                    }}</label
                  >
                </div>
                <br />
              </form>
            </div>

            <br /><br />

            <div class="mastergroup">
              <label for="basic-url" class="form-label"
                ><b>本科毕业去向（读研、工作）相关信息</b></label
              >

              <form class="row g-3">
                <div class="col-md-12">
                  <label for="inputState" class="form-label"
                    >毕业去向类别：{{ master_info.master_desttype }} </label
                  ><br />
                </div>
                <div class="col-md-6">
                  <label for="text" class="form-label"
                    >毕业去向（学校、公司）：{{ master_info.master_dest }}
                  </label>
                </div>
                <div class="col-md-6">
                  <label for="text" class="form-label"
                    >去向城市：{{ master_info.master_city }}
                  </label>
                </div>
                <div class="col-md-6">
                  <label for="inputAddress" class="form-label"
                    >读研专业：{{ master_info.master_major }}
                  </label>
                </div>
                <div class="col-md-6">
                  <label for="inputAddress2" class="form-label"
                    >研究方向：{{ master_info.master_direction }}</label
                  >
                </div>
                <div class="col-md-6">
                  <label for="inputCity" class="form-label"
                    >预计毕业年限：{{ master_info.master_period }} 年
                  </label>
                </div>
                <div class="col-md-6">
                  <label for="inputCity" class="form-label"
                    >硕士或直博：{{ master_info.master_orphd }}
                  </label>
                </div>
              </form>
            </div>
          </div>

          <br />

          <form class="row g-3">
            <div class="col-md-6">
              <button class="btn btn-primary" @click="TryUpdateSelfinfo()">
                更新个人信息
              </button>
            </div>
            <div class="col-md-6">
              <button class="btn btn-primary" @click="TryChangepwd()">
                修改登录密码
              </button>
            </div>
            <!-- <div class="col-md-4">
              <span class="d-inline-block" tabindex="0" data-bs-toggle="popover" data-bs-trigger="hover focus" data-bs-content="Disabled popover">
                <button class="btn btn-danger" type="button" @click="TryDeleteAccount()">永久注销账号</button>
              </span>
            </div> -->
          </form>
        </div>
      </div>
    </div>

    <Footer />
  </div>
</template>

<script>
import Header from "../components/HeaderComp.vue";
import Footer from "../components/FooterComp.vue";
import { GetInfoPost } from "../apis/read.js";
import { DeleteUserAccountPost } from "../apis/update.js";
import { ref, reactive, onMounted } from "@vue/composition-api";
import { useStore } from "vuex";
import Axios from "axios";
import router from "../router";
import store from "../store";

export default {
  name: "SelfinfoView",
  components: {
    Header,
    Footer
  },
  setup(props, context) {
    let stu_permission = reactive({
      permission_type: 3
    });
    const bachelor_info = reactive({
      bachelor_school: "",
      bachelor_city: "",
      bachelor_major: "",
      bachelor_major_trans: "",
      bachelor_major_second: ""
    });
    const master_info = reactive({
      master_desttype: 0,
      master_dest: "",
      master_city: "",
      master_major: "",
      master_direction: "",
      master_orphd: "",
      master_period: ""
    });
    let error_message = reactive("");

    onMounted(() => {
      console.log(context.root.$route.path);
    });

    const testParams = reactive({
      key: "fetchselfinfo",
      stu_uuid: store.state.user.uuid
    });

    GetInfoPost(testParams)
      .then(resp => {
        stu_permission.permission_type = resp.data.data[0]["stu_permission"];
        bachelor_info.bachelor_school = resp.data.data[1]["stu_bachelorschool"];
        bachelor_info.bachelor_city = resp.data.data[1]["stu_bachelorcity"];
        bachelor_info.bachelor_major = resp.data.data[1]["stu_bachelormajor"];
        bachelor_info.bachelor_major_trans =
          resp.data.data[1]["stu_bachelormajornew"];
        bachelor_info.bachelor_major_second =
          resp.data.data[1]["stu_bachelormajorsecond"];
        master_info.master_desttype = resp.data.data[2]["stu_desttype"];
        master_info.master_dest = resp.data.data[2]["stu_dest"];
        master_info.master_city = resp.data.data[2]["stu_city"];
        master_info.master_major = resp.data.data[2]["stu_mastermajor"];
        master_info.master_direction = resp.data.data[2]["stu_direction"];
        master_info.master_orphd = resp.data.data[2]["stu_masterorphd"];
        master_info.master_period = resp.data.data[2]["stu_masterperiod"];
      })
      .catch(err => {
        let error_message =
          "please check the server state and try later.. ErrorCode: " + err;
        alert(error_message);
      });

    return {
      stu_permission,
      bachelor_info,
      master_info,
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
    TryUpdateSelfinfo() {
      router.push({ name: "Manageinfo" });
    },
    TryChangepwd() {
      router.push({ name: "Changepwd" });
    },
    TryDeleteAccount() {
      const postparams = reactive({
        user_uuid: this.$store.state.user.uuid,
        key: "deleteuseraccount"
      });
      DeleteUserAccountPost(postparams)
        .then(resp => {})
        .catch(err => {});
      this.$store.dispatch("LogoutAction", {});
      this.$router.push({ name: "Home" });
    }
  }
};
</script>
