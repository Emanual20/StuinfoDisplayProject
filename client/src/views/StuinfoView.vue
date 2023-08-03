<template>
  <div class="stuinfo">
    <Header />

    <div class="container">
      <div class="card-body">
        <h4>我的班级</h4>
        
        <div class="p-4 mb-4">
          <h5>本科去向</h5>
          <table class="p-4 mb-4 table table-striped table-hover">
            <thead>
              <tr>
                <th scope="col">姓名</th>
                <th scope="col">城市</th>
                <th scope="col">学校</th>
                <th scope="col">专业</th>
                <th scope="col">第二专业</th>
                <th scope="col">最近更新时间</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(niter0, index) in $store.state.nlist.nlist0" :key="index">
                <th scope="col">{{ niter0.stu_name }}</th>
                <th scope="col">{{ niter0.stu_bachelorcity }}</th>
                <th scope="col">{{ niter0.stu_bachelorschool }}</th>
                <th scope="col">{{ niter0.stu_bachelormajor }}</th>
                <th scope="col">{{ niter0.stu_bachelormajorsecond }}</th>
                <th scope="col">{{ niter0.stu_bachelor_lastupd_timestamp }}</th>
              </tr>
            </tbody>
          </table>
        </div>
      
      <div class="p-4 mb-4">
        <h5>本科及后续去向</h5>
        <table class="table table-striped table-hover">
          <thead>
            <tr>
              <th scope="col">姓名</th>
              <th scope="col">城市</th>
              <th scope="col">去向</th>
              <th scope="col">专业/职位</th>
              <th scope="col">方向</th>
              <th scope="col">硕博</th>
              <th scope="col">最近更新时间</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="niter1 in $store.state.nlist.nlist1" :key="niter1.id">
              <th scope="col">{{ niter1.stu_name }}</th>
              <th scope="col">{{ niter1.stu_city }}</th>
              <th scope="col">{{ niter1.stu_dest }}</th>
              <th scope="col">{{ niter1.stu_mastermajor }}</th>
              <th scope="col">{{ niter1.stu_direction }}</th>
              <th scope="col">{{ niter1.stu_masterorphd }}-{{ niter1.stu_masterperiod }}</th>
              <th scope="col">{{ niter1.stu_master_lastupd_timestamp }}</th>
            </tr>
            <tr v-for="niter2 in $store.state.nlist.nlist2" :key="niter2.id">
              <th scope="col">{{ niter2.stu_name }}</th>
              <th scope="col">{{ niter2.stu_city }}</th>
              <th scope="col">{{ niter2.stu_dest }}</th>
              <th scope="col">{{ niter2.stu_mastermajor }}</th>
              <th scope="col">{{ niter2.stu_direction }}</th>
              <th scope="col">{{ niter2.stu_masterorphd }}-{{ niter2.stu_masterperiod }}</th>
              <th scope="col">{{ niter2.stu_master_lastupd_timestamp }}</th>
            </tr>
          </tbody>
        </table>
        </div>
      </div>

      <!-- <MapContainer :params="bachelor_map_params"></MapContainer> -->


    </div>

    <Footer />
  </div>
</template>

<script>
import Header from "../components/HeaderComp.vue";
import Footer from "../components/FooterComp.vue";
import MapContainer from "../components/MapContainer.vue"
import { FetchAdmittedInfoPost } from "../apis/read.js";
import { CheckPwPost } from "../apis/read.js";
import { ref, reactive, onMounted } from "@vue/composition-api";
import store from "../store";
import { shallowRef } from '@vue/reactivity'

export default {
  name: "StuinfoView",
  components: {
    Header,
    Footer,
    MapContainer
  },
  data(){
    return {
    }
  },
  setup(props, context) {
    // fetch positions from database, positions for example
    var positions = [
        [43.24984, 54.879241],
        [85.491458, 132.258452]
    ];
    var zoom = 4;
    var zooms = [2, 22];
    var center = [105.602725,37.076636];
    const bachelor_map_params = reactive({
      positions: positions,
      zoom: zoom,
      zooms: zooms,
      center: center
    });

    const FetchInfoParams = reactive({
      url: "fetchadmittedinfo",
      key: "fetchinfo",
      username: store.state.user.username
    });

    FetchAdmittedInfoPost(FetchInfoParams)
      .then(resp => {
        store.dispatch("UpdateNlistAction", {
          nlist0: resp.data.data[0],
          nlist1: resp.data.data[1],
          nlist2: resp.data.data[2]
        });
      })
      .catch(err => {
        this.text = "error" + err;
        alert(this.text);
      });

    return {
      bachelor_map_params
    };
  },

  methods:{
  },

};
</script>