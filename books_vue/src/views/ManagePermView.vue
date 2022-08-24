<template>
  <div class="managepoerm">
    <Header />

    <div class="container">
      <div class="card-body">
        <div class="permissioninfo">
          <h4><b> 权限管理</b></h4>
          若您想一键修改<b>所有同学</b>对您详细个人信息可查看权限，请使用下述选项（勾选表示可见，反之亦然）。<br />

          <button
            type="button"
            @click.prevent="UpdateAllPermissions()"
            class="btn btn-success"
          >
            确认修改
          </button>
          ps:
          这个按钮是用来修改所有同学查看权限的，只为方便一键修改，如需修改单独权限请点下面一组的button...

          <div class="form-check form-switch">
            <input
              class="form-check-input"
              type="checkbox"
              role="switch"
              v-model="allpermData.permvalue"
              id="allpermData.permvalue"
              checked
            />
            <label class="form-check-label" for="flexSwitchCheckChecked"
              >允许所有同学查看详细信息</label
            >
          </div>

          <br />
          <br />若您想单独修改<b>某个同学</b>对您详细个人信息的查看权限，请使用下述选项（勾选表示可见，反之亦然）。<br />

          <button
            type="button"
            @click.prevent="UpdatePermission()"
            class="btn btn-success"
          >
            确认修改
          </button>
          ps:
          这个按钮是用来修改单个同学查看权限的，如需一键修改所有查看权限请点上面一组的button...

          <div v-for="(niter, index) in studentData.students" :key="index">
            <div class="form-check form-switch">
              <input
                class="form-check-input"
                type="checkbox"
                role="switch"
                v-model="niter['value']"
                id="niter['value']"
                checked
              />
              <label class="form-check-label" for="flexSwitchCheckChecked"
                >允许同学:{{ niter["stu_name"] }} 查看</label
              >
            </div>
          </div>
        </div>
      </div>
    </div>

    <Footer />
  </div>
</template>

<script>
import Header from "../components/HeaderComp.vue";
import Footer from "../components/FooterComp.vue";
import { GetStudents, GetStudentsPermission } from "../apis/read.js";
import { UpdatePermPost } from "../apis/update.js";
import { ref, reactive, onMounted } from "@vue/composition-api";
import Axios from "axios";
import router from "../router";
import store from "../store";

export default {
  name: "ManagePermView",
  components: {
    Header,
    Footer
  },
  setup(props, context) {
    let error_message = "";

    const studentData = reactive({
      students: []
    });

    const allpermData = reactive({
      permvalue: 0
    });

    const GetStudentsPermissionParams = reactive({
      url: "get_all2stuperminfos",
      key: "getpermission",
      stu_uuid: store.state.user.uuid
    });

    GetStudentsPermission(GetStudentsPermissionParams).then(response => {
      studentData.students = response.data.data;
    });

    return {
      studentData,
      allpermData,
      error_message
    };
  },

  data() {
    return {
      text: "hello world to check test() function",
      retCode: -1
    };
  },

  methods: {
    UpdateAllPermissions() {
      const testParams = reactive({
        url: "updateallpermissions",
        key: "update",
        username: this.$store.state.user.username,
        stu_uuid: this.$store.state.user.uuid,
        allpermvalue: this.allpermData.permvalue,
        infos: this.studentData.students
      });
      UpdatePermPost(testParams)
        .then(resp => {
          this.text = resp.data.message;
          console.log(this.text);
          alert("Update All Permission Information Successfully..!");
        })
        .catch(err => {
          this.text = "error" + err;
          console.log(this.text);
        });
    },
    UpdatePermission() {
      const testParams = reactive({
        url: "updatepermission",
        key: "update",
        username: this.$store.state.user.username,
        stu_uuid: this.$store.state.user.uuid,
        infos: this.studentData.students
      });
      UpdatePermPost(testParams)
        .then(resp => {
          this.text = resp.data.message;
          console.log(this.text);
          alert("Update Permission Information Successfully..!");
        })
        .catch(err => {
          this.text = "error" + err;
          console.log(this.text);
        });
    }
  }
};
</script>
