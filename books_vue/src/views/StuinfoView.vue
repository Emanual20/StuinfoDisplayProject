<template>
  <div class="stuinfo">
    <Header />

    <div class="container">
      <div class="card-body">
        <h4><b>查看他人信息</b></h4>
        以下有两个表单，第一个表单用来展示本科相关信息（这个表单不涉及权限，因为之前班群已经发过了，即所有人均可见），第二个表单用来展示本科毕业去向相关信息（<b>这个表单能看到的是按照同学们设定的权限展示，初始生成了10%的可见权限，如果你想(不想)让ta看到，可以随时在权限管理页面修改权限</b>）。<br />
      </div>

      <h5><b>本科相关信息</b></h5>
      <table class="table table-striped table-hover">
        <thead>
          <tr>
            <th scope="col">姓名</th>
            <th scope="col">城市</th>
            <th scope="col">学校</th>
            <th scope="col">专业</th>
            <th scope="col">转入专业</th>
            <th scope="col">第二专业</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(niter0, index) in $store.state.nlist.nlist0" :key="index">
            <th scope="col">{{ niter0.stu_name }}</th>
            <th scope="col">{{ niter0.stu_bachelorcity }}</th>
            <th scope="col">{{ niter0.stu_bachelorschool }}</th>
            <th scope="col">{{ niter0.stu_bachelormajor }}</th>
            <th scope="col">{{ niter0.stu_bachelormajornew }}</th>
            <th scope="col">{{ niter0.stu_bachelormajorsecond }}</th>
          </tr>
        </tbody>
      </table>
      <br /><br />

      <h5><b>本科毕业去向相关信息</b></h5>
      <table class="table table-striped table-hover">
        <thead>
          <tr>
            <th scope="col">姓名</th>
            <th scope="col">城市</th>
            <th scope="col">去向</th>
            <th scope="col">专业（职位）</th>
            <th scope="col">方向</th>
            <th scope="col">硕或博</th>
            <th scope="col">学制</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="niter1 in $store.state.nlist.nlist1" :key="niter1.id">
            <th scope="col">{{ niter1.stu_touuid }}</th>
            <th scope="col">{{ niter1.stu_city }}</th>
            <th scope="col">{{ niter1.stu_dest }}</th>
            <th scope="col">{{ niter1.stu_mastermajor }}</th>
            <th scope="col">{{ niter1.stu_direction }}</th>
            <th scope="col">{{ niter1.stu_masterorphd }}</th>
            <th scope="col">{{ niter1.stu_masterperiod }}</th>
          </tr>
          <tr v-for="niter2 in $store.state.nlist.nlist2" :key="niter2.id">
            <th scope="col">{{ niter2.stu_touuid }}</th>
            <th scope="col">{{ niter2.stu_city }}</th>
            <th scope="col">{{ niter2.stu_dest }}</th>
            <th scope="col">{{ niter2.stu_mastermajor }}</th>
            <th scope="col">{{ niter2.stu_direction }}</th>
            <th scope="col">{{ niter2.stu_masterorphd }}</th>
            <th scope="col">{{ niter2.stu_masterperiod }}</th>
          </tr>
        </tbody>
      </table>
    </div>

    <Footer />
  </div>
</template>

<script>
import Header from "../components/HeaderComp.vue";
import Footer from "../components/FooterComp.vue";
import { FetchAdmittedInfoPost } from "../apis/read.js";
import { CheckPwPost } from "../apis/read.js";
import { ref, reactive, onMounted } from "@vue/composition-api";
import store from "../store";

export default {
  name: "StuinfoView",
  components: {
    Header,
    Footer
  },
  setup(props, context) {
    onMounted(() => {
      console.log(context.root.$route.path);
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

    return {};
  },

  data() {
    return {
      text: "hello world to check test() function"
    };
  },

  methods: {}
};
</script>
