<template>
    <div class="stuinfo">
      <Header />
  
      <div class="container">
        <div class="card-body">
          <div class="p-2 mb-2">
              <h5>地图预览 - 高考去向 </h5>
              <a>目前地图只能展示国内坐标，且会有一定位置误差，后续修正。</a>
          </div>
  
          <div class="p-4 mb-4" style="display: flex; justify-content: center; align-items: center;">
              <MapContainer :params="bachelor_map_params"></MapContainer>
            </div>
          
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
  import MapContainer from "../components/MapContainer.vue";
  import { FetchMapInfo } from "../apis/read.js";
  import { CheckPwPost } from "../apis/read.js";
  import { ref, reactive, onMounted } from "@vue/composition-api";
  import store from "../store";
  import { shallowRef } from '@vue/reactivity'
  
  export default {
    name: "MapView",
    components: {
      Header,
      Footer,
      MapContainer,
    },
    setup(props, context) {
      const FetchInfoParams = reactive({
        url: "fetchmapinfo",
        key: "fetchinfo",
        username: store.state.user.username
      });
  
      FetchMapInfo(FetchInfoParams)
        .then(resp => {
          store.dispatch("UpdateNmapAction", {
            nmap: resp.data.data[0],
          });
        })
        .catch(err => {
          this.text = "error" + err;
          alert(this.text);
        });
      
      // fetch positions from database, positions for example
      var bachelor_positions = [
        [117.17166, 39.13105]
      ];
  
      var zoom = 5;
      var zooms = [3, 18];
  
      var bachelor_center = [113.665412,34.757975];
      const bachelor_map_params = reactive({
        positions: store.state.nlist.nmap,
        zoom: zoom,
        zooms: zooms,
        center: bachelor_center
      });
  
      return {
        bachelor_map_params,
      };
    },
  
    methods:{
    },
  
  };
  </script>