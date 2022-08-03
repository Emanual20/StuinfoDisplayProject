<template>
<div id="NotFound">
    <Header />
    <b-container class="mt-4 mb-2">
        Invalid request...
        Please check your request URL...
    </b-container>
    <Footer />
</div>
</template>

<script>
import Header from "../components/HeaderComp.vue";
import Footer from "../components/FooterComp.vue";

export default {
    name:"NotFoundView",
    components:{
        Header,
        Footer,
    },
}
</script>

<style lang="scss" scoped>

</style>