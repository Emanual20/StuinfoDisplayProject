import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: {
      username: "",
      password: "",
      uuid: "",
      fullName: "",
      is_login: false
    },
    nlist: {
      nlist0: [], // bachelor info
      nlist1: [], // graduation info admitted
      nlist2: [], // graduation info forbiddened
      nmap: [] // map data needed
    },
    spitslot: {
      data: [], // recent spitslot info
    }
  },
  mutations: {
    UpdateUserStateMuta(state, user) {
      state.user.username = user.username;
      state.user.password = user.password;
      state.user.uuid = user.uuid;
      state.user.is_login = user.is_login;
    },
    LogoutMuta(state) {
      state.user.username = "";
      state.user.password = "";
      state.user.uuid = "";
      state.user.is_login = false;
      state.nlist.nlist0 = [];
      state.nlist.nlist1 = [];
      state.nlist.nlist2 = [];
    },
    UpdateNlistMuta(state, nlist) {
      state.nlist.nlist0 = nlist.nlist0;
      state.nlist.nlist1 = nlist.nlist1;
      state.nlist.nlist2 = nlist.nlist2;
    },
    UpdateNmapMuta(state, nlist){
      state.nlist.nmap = nlist.nmap;
    },
    UpdateSpitslotMuta(state, ndata){
      state.spitslot.data = ndata.ndata;
    }
  },
  actions: {
    UpdateUserStateAction(context, user) {
      context.commit("UpdateUserStateMuta", {
        username: user.username,
        password: user.password,
        uuid: user.uuid,
        is_login: user.is_login
      });
    },
    LogoutAction(context) {
      context.commit("LogoutMuta");
    },
    UpdateNlistAction(context, nlist) {
      context.commit("UpdateNlistMuta", {
        nlist0: nlist.nlist0,
        nlist1: nlist.nlist1,
        nlist2: nlist.nlist2
      });
    },
    UpdateNmapAction(context, nlist) {
      context.commit("UpdateNmapMuta", {
        nmap: nlist.nmap,
      });
    },    
    UpdateSpitslot(context, ndata){
      context.commit("UpdateSpitslotMuta", {
        ndata: ndata
      });
    }
  },
  modules: {}
});
