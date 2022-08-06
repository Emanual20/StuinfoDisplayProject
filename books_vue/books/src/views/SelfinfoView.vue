<template>
<div id="NotFound">
    <Header />
    <b-container class="mt-4 mb-2">
        <b>
        我没有做这个页面...<br>
        但是你可以通过先进入 权限管理 页面给自己读权限（因为随机生成权限的时候可能不会生成你给自己的读权限），然后再去 查看信息 页面就能看见自己了..<br> 
        是不是很方便！是的！（超大声）<br>
        </b>
    </b-container>
    <Footer />
</div>
</template>

<script>
import Header from "../components/HeaderComp.vue";
import Footer from "../components/FooterComp.vue";

export default {
    name:"SelfinfoView",
    components:{
        Header,
        Footer,
    },
}
</script>

<style lang="scss" scoped>

</style>