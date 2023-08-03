<template>
  <div class="manageinfo">
    <Header />

    <div class="container">
      <div class="card-body">
        <div class="personalinfo">
          <h4>更新信息</h4>
          <br />

          <div class="border border-light-subtle p-4 mb-4 border-opacity-50 bachelorgroup">
            <label for="basic-url" class="form-label"
              ><b>本科相关信息</b></label
            >
            <br />
            <label for="basic-url" class="form-label"
              >以下内容带*的内容为<b>必填项</b>，其余不设置合法检查，请根据提示填写。</label
            >
            <br />

            <form class="row g-3 p-2 mb-2">
              <div class="col-md-6">
                <label for="text" class="form-label">本科学校<b>*</b></label>
                <input
                  type="text"
                  v-model="bachelor_school"
                  class="form-control"
                  id="bachelor_school"
                  placeholder="如：清华大学，南开大学等"
                />
              </div>
              <div class="col-md-6">
                <label for="inputCity" class="form-label"
                  >本科城市<b>*</b></label
                >
                <input
                  type="text"
                  v-model="bachelor_city"
                  class="form-control"
                  id="bachelor_city"
                  placeholder="如：北京，天津等"
                />
              </div>
              <div class="col-md-4">
                <label for="text" class="form-label">本科专业</label>
                <input
                  type="text"
                  v-model="bachelor_major"
                  class="form-control"
                  id="bachelor_major"
                  placeholder="如：数学，土木工程等"
                />
              </div>
              <div class="col-md-4">
                <label for="text" class="form-label">本科转入专业</label>
                <input
                  type="text"
                  v-model="bachelor_major_trans"
                  class="form-control"
                  id="bachelor_major_trans"
                  placeholder="如：金融工程，计算机科学与技术等"
                />
              </div>
              <div class="col-md-4">
                <label for="text" class="form-label"
                  >本科二专业（双学位、辅修）</label
                >
                <input
                  type="text"
                  v-model="bachelor_major_second"
                  class="form-control"
                  id="bachelor_major_second"
                  placeholder="如：哲学，心理学等"
                />
              </div>
              <div class="col-12">
                <div class="form-check">
                  <label class="form-check-label" for="gridCheck">
                    <b></b>
                  </label>
                </div>
              </div>
              <div class="col-12">
                <button
                  @click.prevent="update_bachelor()"
                  type="submit"
                  class="btn btn-primary"
                >
                  更新
                </button>
              </div>
            </form>
          </div>

          <br />

          <div class="border border-light-subtle p-4 mb-4 border-opacity-50 mastergroup">
            <label for="basic-url" class="form-label"
              ><b>本科毕业去向（读研、工作）相关信息</b></label
            >
            <br />
            <label for="basic-url" class="form-label"
              >以下内容不设置合法检查，请根据提示填写。</label
            >

            <form class="row g-3 p-2 mb-2">
              <div class="col-md-12">
                <label for="inputState" class="form-label"
                  >毕业去向类别<b>*</b></label
                ><br />
                <select
                  id="master_desttype"
                  v-model="master_desttype"
                  class="form-select"
                >
                  <option value="0">未知</option>
                  <option value="1">升学-非内地（出国，港澳台等地区）</option>
                  <option value="2">升学-内地</option>
                  <option value="3">工作</option>
                  <option value="4">待定</option>
                </select>
              </div>
              <div class="col-md-6">
                <label for="text" class="form-label"
                  >毕业去向（学校、公司）<b>*</b></label
                >
                <input
                  type="text"
                  class="form-control"
                  v-model="master_dest"
                  id="master_dest"
                  placeholder="如：斯坦福大学，中建一局等（最好写全称）"
                />
              </div>
              <div class="col-md-6">
                <label for="text" class="form-label">去向城市<b>*</b></label>
                <input
                  type="text"
                  class="form-control"
                  v-model="master_city"
                  id="master_city"
                  placeholder="如：天津，洛杉矶等"
                />
              </div>
              <div class="col-md-6">
                <label for="inputAddress" class="form-label">专业/岗位</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="master_major"
                  id="master_major"
                  placeholder="如：计算机科学与技术，法务/销售等"
                />
              </div>
              <div class="col-md-6">
                <label for="inputAddress2" class="form-label">研究方向</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="master_direction"
                  id="master_direction"
                  placeholder="如：模式识别，偏微分方程等"
                />
              </div>
              <div class="col-md-6">
                <label for="inputCity" class="form-label"
                  >预计毕业年限（以年为单位）</label
                >
                <input
                  type="text"
                  class="form-control"
                  v-model="master_period"
                  id="master_period"
                  placeholder="如：2.5，3等"
                />
              </div>
              <div class="col-md-6">
                <label for="inputCity" class="form-label">硕士或直博</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="master_orphd"
                  id="master_orphd"
                  placeholder="如：RA、硕士、学硕、专硕、直博等"
                />
              </div>

              <div class="col-12">
                <div class="form-check">
                  <label class="form-check-label" for="gridCheck"></label>
                </div>
              </div>
              <div class="col-12">
                <button
                  @click.prevent="update_master()"
                  type="submit"
                  class="btn btn-primary"
                >
                  更新
                </button>
              </div>
            </form>
          </div>

          <br /><br />
        </div>
      </div>
    </div>

    <Footer />
  </div>
</template>

<script>
import Header from "../components/HeaderComp.vue";
import Footer from "../components/FooterComp.vue";

import { CheckPwPost } from "../apis/read.js";
import { UpdateInfoPost } from "../apis/update.js";
import { ref, reactive, onMounted } from "@vue/composition-api";
import { useStore } from "vuex";
import Axios from "axios";
import router from "../router";
import store from "../store";

export default {
  name: "ManageInfoView",
  components: {
    Header,
    Footer
  },
  setup(props, context) {
    let username = "";
    let bachelor_school = "";
    let bachelor_city = "";
    let bachelor_major = "";
    let bachelor_major_trans = "";
    let bachelor_major_second = "";
    let error_message = "";

    let master_desttype = 0;
    let master_dest = "";
    let master_city = "";
    let master_major = "";
    let master_direction = "";
    let master_orphd = "";
    let master_period = "";

    return {
      username,
      bachelor_school,
      bachelor_city,
      bachelor_major,
      bachelor_major_trans,
      bachelor_major_second,
      master_desttype,
      master_desttype,
      master_dest,
      master_city,
      master_major,
      master_direction,
      master_orphd,
      master_period,
      error_message
    };
  },

  data() {
    return {
      text: "hello world to check test() function",
      retCode: -1,
    };
  },

  methods: {
    update_bachelor() {
      const testParams = reactive({
        url: "updatebachelorinfo",
        key: "update",
        username: this.$store.state.user.username,
        infos: {
          bachelor_school: bachelor_school.value,
          bachelor_city: bachelor_city.value,
          bachelor_major: bachelor_major.value,
          bachelor_major_trans: bachelor_major_trans.value,
          bachelor_major_second: bachelor_major_second.value
        }
      });
      UpdateInfoPost(testParams)
        .then(resp => {
          alert("Success..!");
        })
        .catch(err => {
        });
    },
    update_master() {
      const testParams = reactive({
        url: "updatemasterinfo",
        key: "update",
        username: this.$store.state.user.username,
        infos: {
          master_desttype: master_desttype.value,
          master_dest: master_dest.value,
          master_city: master_city.value,
          master_major: master_major.value,
          master_direction: master_direction.value,
          master_orphd: master_orphd.value,
          master_period: master_period.value
        }
      });
      UpdateInfoPost(testParams)
        .then(resp => {
          alert("Success..!");
        })
        .catch(err => {
        });
    },
  }
};
</script>

<style>
</style>