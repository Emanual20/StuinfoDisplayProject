<template>
  <div id="SpitslotView">
    <Header />
    <b-container>
      <div class="container">
        <div class="card-body">
          <h4><b>我要吐槽</b></h4>
          <form @submit.prevent="updatespitslot()">
            <div class="form-group">
              <textarea
                class="form-control"
                rows="3"
                v-model="textinfo"
                placeholder="任何内容都可以！"
              >
              </textarea>
            </div>
            <button type="submit" class="btn btn-primary">上传</button>
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
import { UploadSpitslotPost } from "../apis/update.js";
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
    let error_message = "";
    let textinfo = "";
    onMounted(() => {
      console.log(context.root.$route.path);
    });
    return {
      error_message,
      textinfo
    };
  },
  methods: {
    updatespitslot() {
      const testParams = reactive({
        url: "/updatespitslot",
        key: "updatespitslot",
        stu_uuid: this.$store.state.user.uuid,
        info: this.textinfo
      });
      UploadSpitslotPost(testParams)
        .then(resp => {
          this.text = resp.data.message;
          alert(this.text);
        })
        .catch(err => {
          let error_message = "Internal server error.." + err;
          alert(error_message);
        });
    }
  }
};
</script>

<style lang="scss" scoped></style>
