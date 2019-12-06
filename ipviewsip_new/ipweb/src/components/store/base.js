import Vue from 'vue'
import Cookie from 'vue-cookies'
const state = {
  tableData:{},
  Title:'',
  ID:'/',
  loading:false,
  b_loading:false,
  All:{
    "all":{'service':{
          'memorytotal':0,
          'memoryuse':0,
          'memoryrate':0,
          'disktotal':0,
          'diskuse':0,
          'diskrate':0,
          'cpurate':0},
      'bigdata':{
          'memorytotal':0,
          'memoryuse':0,
          'memoryrate':0,
          'disktotal':0,
          'diskuse':0,
          'diskrate':0,
          'cpurate':0
      }
    }},
  Ip:{"phycount":0,"servertotalcount":0,"vircount":0},
  Home:{ "ip_all": 0,
        "e_all": 0,
        "v_all": 0,
        "p_all": 0,
  }
};

const mutations = {
  set_base_list(state,newdata){
      state.tableData = newdata;
    },
  set_b_loading(state,newdata){
      state.b_loading = newdata;
    },
  set_title(state,newdata){
      state.Title = newdata;
      console.log(newdata,"test");
      // this.$cookies.set("Title",newdata.e+" / "+newdata.b)
    },
  set_loading(state,newdata){
      state.loading = newdata;
    },
  set_id(state,newdata){
      state.ID = newdata;
    },
  set_ip(state,newdata){
      state.Ip = newdata;
    },
  set_all(state,newdata){
      state.All = newdata;
    },
  set_home(state,newdata){
      state.Home = newdata;
    },
};
const actions = {
  base_list({state, commit, rootState}){
    Vue.http.get(Vue.baseConfig.request_url+"/api/v1/base_info",{
    }).then(function (resp){
      commit("set_base_list",resp.data);
      console.log(resp.data)
    })
  },
  get_ip_list({state, commit, rootState},data){
    commit("set_loading",true);
    Cookie.set("Title",data.b+"/"+data.e);
    if(data.id){
      Cookie.set("ID",data.id);
      commit("set_id",data.id);
    }
    commit("set_title",data.b+"/"+data.e);

    Vue.http.get(Vue.baseConfig.request_url+"/api/v1/ip_info",{
      params:data
    }).then(function (resp) {
      console.log(resp.data);
      commit("set_ip",resp.data);
      commit("set_loading",false);
    })
  },
  get_all_list({state, commit, rootState},data) {
    Vue.http.get(Vue.baseConfig.request_url + "/api/v1/all_info", {
      params: data
    }).then(function (resp) {
      console.log(resp.data);
      commit("set_all",resp.data);
    });
  },
  download({state, commit, rootState},data){
    commit("set_b_loading",true);
    Vue.http.get(Vue.baseConfig.request_url + "/api/v1/download", {
      params: data,
    responseType: 'blob'},).then(function (resp) {
      console.log(resp);
      if(resp.data.type === 'application/json'){
        console.log("没有");
        window.app.$message({message:'此日期下没有报表',type:'error'});
        commit("set_b_loading",false);
      }else {
        commit("set_b_loading",false);
        // new Blob([data])用来创建URL的file对象或者blob对象
        let url = window.URL.createObjectURL(new Blob([resp.data]));
        // 生成一个a标签
        let link = document.createElement("a");
        link.style.display = "none";
        link.href = url;
        // 生成时间戳
        let timestamp = new Date().getTime();
        link.download = "ipdatas.xlsx";
        document.body.appendChild(link);
        link.click();
      }
    })
  },
  get_home({state, commit, rootState},data){
    Vue.http.get(Vue.baseConfig.request_url + "/api/v1/home", {
      params: data
    }).then(function (resp) {
      commit("set_home",resp.data);
      let myChart = Vue.echarts.init(document.getElementById('container'));
            myChart.setOption({
            title:{
              text:"各事业部使用服务器数量"
            },
            legend: {},
            tooltip: {},
			dataset: {
				source: state.Home.b_list
			},
            color: ['#3398DB','#005700'],

            xAxis : [
                {
                    type : 'category',

                      axisLabel:{
                        interval:0,//横轴信息全部显示
                        rotate:-15,//-15度角倾斜显示
                        },
                }
            ],
            yAxis : [
                {
                    type : 'value'
                }
            ],
            series : [
              {
                name: "物理机",
                type: 'bar',
                itemStyle: {
                normal: {
                    label: {
                      show: true,
                      position: 'top',
                      textStyle: {
                        color: 'black',
                        fontSize:16
                      }
                    },
                  }
                }
              },
                            {
                name: '虚拟机',
                type: 'bar',
                itemStyle: {
                normal: {
                    label: {
                      show: true,
                      position: 'top',
                      textStyle: {
                        color: 'black',
                        fontSize:16
                      }
                    },
                  }
                }
              }
            ]
      });
    })
  }
};


export default {
  state,
  actions,
  mutations
}
