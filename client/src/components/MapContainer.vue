<template>
    <div id="container"></div>
</template>

<style scoped>
#container{
  padding: 0px;
  margin: 0px;
  width: 60%;
  height: 600px;
}
</style>

<script>
// attention, you should export by ``{sth}'' only when there is export module exactly named sth, otherwise it is just an alternative name of exported module
import AMapLoader from '@amap/amap-jsapi-loader';
import { shallowRef } from '@vue/reactivity'

export default {
    name:"MapContainer",
    props:['params'],
    setup(){
        const map = shallowRef(null);
        return{
            map,
        }

    },
    create(){

    },
    methods:{
        initMap(){
            AMapLoader.load({
                key:'e4cea3dd984caafc35ca22d01f3ed807',
                version:"2.0",
                plugins:['AMap.ToolBar','AMap.Driving'],
                AMapUI:{
                    version:"1.1",
                    plugins:[],

                },
                Loca:{
                    version:"2.0.0"
                },
            }).then((AMap)=>{
                this.map = new AMap.Map("container",{
                    viewMode:"3D",
                    zoom:this.params.zoom,
                    zooms:this.params.zooms,
                    center:this.params.center,
                });
                console.log("mapcontainer:", this.params)
                let positionArr = [
                    [113.357224,34.977186],
                    [114.555528,37.727903],
                    [112.106257,36.962733],
                    [109.830097,31.859027],
                    [116.449181,39.98614],
                ];
                if(typeof(this.params.positions) == "undefined"){
                    this.params.positions = positionArr;
                    console.log("there is no point! these displayed points are fake! -- by MapContainer.vue")
                }
                for(let item of this.params.positions){
                    let marker = new AMap.Marker({
                        position:[item[0],item[1]],
                    });
                    this.map.add(marker);
                }


            }).catch(e=>{
                console.log(e);
            })
        },
        addMarker(){
            
        }
    },
    mounted(){
        this.initMap();
    }
}

</script>