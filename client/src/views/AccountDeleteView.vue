<template>
    <div class="managepoerm">
      <Header />
  
      <div class="container">
        <div class="card-body">
          <div class="permissioninfo">
            <h4><b> 账号注销</b></h4>
            <div class="p-4 mb-4">
              您将<b>永久注销</b>在本网站的信息，且不可再次注册。<b>此操作不可逆，请思考后谨慎操作！</b>
            </div>
            
            <div class="p-3 mb-3">
                <button
                    type="button"
                    @click.prevent="NotDelete()"
                    class="btn btn-success float-left"
                  >
                    不注销
                </button>
                <button
                  type="button"
                  @click.prevent="TryDeleteAccount()"
                  class="btn btn-danger float-right"
                >
                  确定永久注销
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
  import { DeleteUserAccountPost } from "../apis/update.js";
  import { ref, reactive, onMounted } from "@vue/composition-api";
  import Axios from "axios";
  import router from "../router";
  import store from "../store";
  
  export default {
    name: "DeleteAccount",
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
        NotDelete(){
            this.$router.push({ name: "Selfinfo" });
        },
        TryDeleteAccount(){
            const postparams = reactive({
                key: "deleteuseraccount",
                user_uuid: this.$store.state.user.uuid,
                url: "deleteuseraccount"
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
  