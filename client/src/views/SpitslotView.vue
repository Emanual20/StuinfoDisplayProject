<template>
  <div id="SpitslotView">
    <Header />
    <b-container>
      <div class="container">
        <div class="card-body">
          <h4>匿名吐槽</h4>
          <form @submit.prevent="updatespitslot()">
            <div class="form-group p-3 mb-3">
              <textarea
                class="form-control"
                rows="3"
                v-model="textinfo"
                placeholder="任何内容都可以！"
              >
              </textarea>
            </div>
            <button type="submit" class="btn btn-danger float-right">吐槽</button>
          </form>
          <br><br>
          <h4>历史吐槽</h4>
          <div class="border border-light-subtle p-3 mb-3 border-opacity-50">
            <div class="card mt-4 mb-4" v-for="niter in spitslots.value" :key="niter.id">
              <h5 class="card-header"> {{ niter["spit_timestamp"] }} </h5>
              <div class="card-body">
                <p class="card-text"> {{ niter["spit_info"] }} </p>
              </div>
            </div>
          </div>
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
import { FetchRecentSpitslot } from "../apis/read.js";
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
    let textinfo = "";
    var spitslots = ref([]);

    const FetchSpitslotParams = reactive({
      url: "recentspitslot",
      username: store.state.user.username,
      spitslot_num: 20
    });

    FetchRecentSpitslot(FetchSpitslotParams)
    .then(resp => {
      spitslots.value = resp.data.data;
    })
    .catch(err => {      
    })

    return {
      textinfo,
      spitslots
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
          console.log(this.spitslots.value);
          this.spitslots.value.unshift({
            "spit_id": this.spitslots.value[0]["spit_id"] + 1,
            "spit_info": this.textinfo,
            "spit_timestamp": "Recent",
            "stu_uuid": "undefined"
          });
          alert("Success..!");
        })
        .catch(err => {
        });
    }
  }
};
</script>

<style lang="scss" scoped></style>
