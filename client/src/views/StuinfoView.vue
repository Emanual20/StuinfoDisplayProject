<template>
  <div class="stuinfo">
    <Header />

    <div class="container">
      <div class="card-body">
        <div class="p-2 mb-2">
          <b>我的班级</b>

          <div class="float-right">
            <a @click="display_bachelor()" class="float">高考去向</a> <a @click="display_dest()" class="float">未来去向</a> 
          </div>
        </div>

        <template v-if="display_option.value === '高考去向'">

          
          <div class="p-4 mb-4" style="height: 500px; overflow-y: auto;  width: 100%; overflow-x: auto;">
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


        </template>

        <template v-else-if="display_option.value === '未来去向'">



          <div class="p-4 mb-4" style="height: 500px; overflow-y: auto; width: 100%; overflow-x: auto;">
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
        </template>

        <template v-else>
          nothing display for you.
        </template>

      <div class="p-4 mb-4">
      </div>

    </div>
    </div>

    <Footer />
  </div>
</template>

<script>
import Header from "../components/HeaderComp.vue";
import Footer from "../components/FooterComp.vue";
// import MapContainer from "../components/MapContainer.vue";
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
    // MapContainer,
  },
  setup(props, context) {
    var display_option = ref('高考去向');
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
    
    // fetch positions from database, positions for example
    // var bachelor_positions = [
    //   [117.17166, 39.13105]
    // ];

    // console.log("before:", bachelor_positions, store.state.nlist.nlist0);

    // for (const item of store.state.nlist.nlist0){
    //   var item_posx = item.stu_bachelorxpos;
    //   var item_posy = item.stu_bachelorypos;
    //   if (item_posx === null || item_posy === null){
    //     continue;
    //   }
    //   else{
    //     bachelor_positions.push([item_posx, item_posy]);
    //   }
    // }

    // var dest_positions = [
    //   [117.17166, 39.13105]
    // ];

    // for (const item of store.state.nlist.nlist1){
    //   var item_posx = item.stu_masterxpos;
    //   var item_posy = item.stu_masterypos;
    //   if (item_posx === null || item_posy === null){
    //     continue;
    //   }
    //   else{
    //     dest_positions.push([item_posx, item_posy]);
    //   }
    // }
    // for (const item of store.state.nlist.nlist2){
    //   var item_posx = item.stu_masterxpos;
    //   var item_posy = item.stu_masterypos;
    //   if (item_posx === null || item_posy === null){
    //     continue;
    //   }
    //   else{
    //     dest_positions.push([item_posx, item_posy]);
    //   }
    // }

    // var zoom = 5;
    // var zooms = [3, 18];

    // var bachelor_center = [113.665412,34.757975];
    // const bachelor_map_params = reactive({
    //   positions: bachelor_positions,
    //   zoom: zoom,
    //   zooms: zooms,
    //   center: bachelor_center
    // });

    // var dest_center = [113.665412,34.757975];
    // const dest_map_params = reactive({
    //   positions: dest_positions,
    //   zoom: zoom,
    //   zooms: zooms,
    //   center: dest_center
    // });    

    return {
      display_option,
      // bachelor_map_params,
      // dest_map_params
    };
  },

  methods:{
    display_bachelor(){
      this.display_option.value = "高考去向";
    },
    display_dest(){
      this.display_option.value = "未来去向";
    }
  },

};
</script>