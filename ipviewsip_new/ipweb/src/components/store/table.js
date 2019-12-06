import Vue from 'vue'
const state = {

};

const mutations = {
  set_base_list(state,newdata){
      state.tableData = newdata;
    },
};
const actions = {
  get_memory({state, commit, rootState},data){
    Vue.http.get(Vue.baseConfig.request_url + "/api/v1/memory", {
      params: data
    }).then(function (resp) {
      let myChart = Vue.echarts.init(document.getElementById('memory'));

      var data1 = resp.data;
      myChart.setOption({backgroundColor: new Vue.echarts.graphic.RadialGradient(0, 0, 0, [{
        offset: 0,
        color: '#f7f8fa'
    }, {
        offset: 1,
        color: '#cdd0d5'
    }]),
    title: {
        text: '内存使用率分布情况'
    },
    legend: {
        right: 10,
        data: ['大数据服务器', '应用服务器']
    },
    xAxis: {
        max:100,
        name:"使用率",
        splitLine: {
            lineStyle: {
                type: 'dashed'
            }
        },
    },
    yAxis: {
        name:"服务器id",
        splitLine: {
            lineStyle: {
                type: 'dashed'
            }
        },
        scale: true
    },
    series: [{
        name: '大数据服务器',
        data: data1[0],
        type: 'scatter',
        symbolSize: function (data) {
            return 30;
        },
        label: {
            emphasis: {
                show: true,
                formatter: function (param) {
                    return param.data[2];
                },
                position: 'top',
            }
        },
        itemStyle: {
            normal: {
                shadowBlur: 10,
                shadowColor: 'rgba(120, 36, 50, 0.5)',
                shadowOffsetY: 5,
                color: new Vue.echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                    offset: 0,
                    color: 'rgb(251, 118, 123)'
                }, {
                    offset: 1,
                    color: 'rgb(204, 46, 72)'
                }]),
            },

        }
    }, {
        name: '应用服务器',
        data: data1[1],
        type: 'scatter',
        symbolSize: function (data) {
            return 30;
        },
        label: {
            emphasis: {
                show: true,
                formatter: function (param) {
                    return param.data[2];
                },
                position: 'top'
            }
        },
        itemStyle: {
            normal: {
                shadowBlur: 10,
                shadowColor: 'rgba(25, 100, 150, 0.5)',
                shadowOffsetY: 5,
                color: new Vue.echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                    offset: 0,
                    color: 'rgb(129, 227, 238)'
                }, {
                    offset: 1,
                    color: 'rgb(25, 183, 207)'
                }]),
            }
        }
    }]
}
            );
    })
  },
  get_disk({state, commit, rootState},data){
    Vue.http.get(Vue.baseConfig.request_url + "/api/v1/disk", {
      params: data
    }).then(function (resp) {
      let myChart = Vue.echarts.init(document.getElementById('disk'));

      var data1 = resp.data;
      myChart.setOption({backgroundColor: new Vue.echarts.graphic.RadialGradient(0, 0, 0, [{
        offset: 0,
        color: '#f7f8fa'
    }, {
        offset: 1,
        color: '#cdd0d5'
    }]),
    title: {
        text: '磁盘使用率分布情况'
    },
    legend: {
        right: 10,
        data: ['大数据服务器', '应用服务器']
    },
    xAxis: {
        max:100,
        name:"使用率",
        splitLine: {
            lineStyle: {
                type: 'dashed'
            }
        },
    },
    yAxis: {
        name:"服务器id",
        splitLine: {
            lineStyle: {
                type: 'dashed'
            }
        },
        scale: true
    },
    series: [{
        name: '大数据服务器',
        data: data1[0],
        type: 'scatter',
        symbolSize: function (data) {
            return 30;
        },
        label: {
            emphasis: {
                show: true,
                formatter: function (param) {
                    return param.data[2];
                },
                position: 'top',
            }
        },
        itemStyle: {
            normal: {
                shadowBlur: 10,
                shadowColor: 'rgba(120, 36, 50, 0.5)',
                shadowOffsetY: 5,
                color: new Vue.echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                    offset: 0,
                    color: 'rgb(251, 118, 123)'
                }, {
                    offset: 1,
                    color: 'rgb(204, 46, 72)'
                }]),
            },

        }
    }, {
        name: '应用服务器',
        data: data1[1],
        type: 'scatter',
        symbolSize: function (data) {
            return 30;
        },
        label: {
            emphasis: {
                show: true,
                formatter: function (param) {
                    return param.data[2];
                },
                position: 'top'
            }
        },
        itemStyle: {
            normal: {
                shadowBlur: 10,
                shadowColor: 'rgba(25, 100, 150, 0.5)',
                shadowOffsetY: 5,
                color: new Vue.echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                    offset: 0,
                    color: 'rgb(129, 227, 238)'
                }, {
                    offset: 1,
                    color: 'rgb(25, 183, 207)'
                }]),
            }
        }
    }]
}
            );
    })
  },
  get_cpu({state, commit, rootState},data){
    Vue.http.get(Vue.baseConfig.request_url + "/api/v1/cpu", {
      params: data
    }).then(function (resp) {
      let myChart = Vue.echarts.init(document.getElementById('cpu_table'));

      var data1 = resp.data;
      myChart.setOption({backgroundColor: new Vue.echarts.graphic.RadialGradient(0, 0, 0, [{
        offset: 0,
        color: '#f7f8fa'
    }, {
        offset: 1,
        color: '#cdd0d5'
    }]),
    title: {
        text: 'cpu使用率分布情况'
    },
    legend: {
        right: 10,
        data: ['大数据服务器', '应用服务器']
    },
    xAxis: {
        max:100,
        name:"使用率",
        splitLine: {
            lineStyle: {
                type: 'dashed'
            }
        },
    },
    yAxis: {
        name:"服务器id",
        splitLine: {
            lineStyle: {
                type: 'dashed'
            }
        },
        scale: true
    },
    series: [{
        name: '大数据服务器',
        data: data1[0],
        type: 'scatter',
        symbolSize: function (data) {
            return 30;
        },
        label: {
            emphasis: {
                show: true,
                formatter: function (param) {
                    return param.data[2];
                },
                position: 'top',
            }
        },
        itemStyle: {
            normal: {
                shadowBlur: 10,
                shadowColor: 'rgba(120, 36, 50, 0.5)',
                shadowOffsetY: 5,
                color: new Vue.echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                    offset: 0,
                    color: 'rgb(251, 118, 123)'
                }, {
                    offset: 1,
                    color: 'rgb(204, 46, 72)'
                }]),
            },

        }
    }, {
        name: '应用服务器',
        data: data1[1],
        type: 'scatter',
        symbolSize: function (data) {
            return 30;
        },
        label: {
            emphasis: {
                show: true,
                formatter: function (param) {
                    return param.data[2];
                },
                position: 'top'
            }
        },
        itemStyle: {
            normal: {
                shadowBlur: 10,
                shadowColor: 'rgba(25, 100, 150, 0.5)',
                shadowOffsetY: 5,
                color: new Vue.echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                    offset: 0,
                    color: 'rgb(129, 227, 238)'
                }, {
                    offset: 1,
                    color: 'rgb(25, 183, 207)'
                }]),
            }
        }
    }]
}
            );
    })
  },
  get_rate_0({state, commit, rootState},data){
    Vue.http.get(Vue.baseConfig.request_url + "/api/v1/rate", {
      params: data
    }).then(function (resp) {
      var data =resp.data;
      let cpu_myChart = Vue.echarts.init(document.getElementById('cpu_rate_0'));
      let disk_myChart = Vue.echarts.init(document.getElementById('disk_rate_0'));
      let mem_myChart = Vue.echarts.init(document.getElementById('mem_rate_0'));

      cpu_myChart.setOption({
    title : {
        text: '应用类主机的cpu使用率分布',
        subtext: '资源分布占比',
        x:'center'
    },
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}% 台)"
    },
    legend: {
        orient: 'vertical',
        left: 'left',
        data: data.title[2]
    },
    series : [
        {
            name: 'cpu资源',
            type: 'pie',
            radius : '55%',
            center: ['50%', '60%'],
            data:data.data[2],
            itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
});
      disk_myChart.setOption({
    title : {
        text: '应用类主机的磁盘使用率分布',
        subtext: '资源分布占比',
        x:'center'
    },
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}% 台)"
    },
    legend: {
        orient: 'vertical',
        left: 'left',
        data: data.title[1]
    },
    series : [
        {
            name: '磁盘资源',
            type: 'pie',
            radius : '55%',
            center: ['50%', '60%'],
            data:data.data[1],
            itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
});
      mem_myChart.setOption({
    title : {
        text: '应用类主机的内存使用率分布',
        subtext: '资源分布占比',
        x:'center'
    },
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}% 台)"
    },
    legend: {
        orient: 'vertical',
        left: 'left',
        data: data.title[0]
    },
    series : [
        {
            name: '内存资源',
            type: 'pie',
            radius : '55%',
            center: ['50%', '60%'],
            data:data.data[0],
            itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
});
    })
  },
  get_rate_1({state, commit, rootState},data){
    Vue.http.get(Vue.baseConfig.request_url + "/api/v1/rate", {
      params: data
    }).then(function (resp) {
      var data =resp.data;
      let cpu_myChart = Vue.echarts.init(document.getElementById('cpu_rate_1'));
      let disk_myChart = Vue.echarts.init(document.getElementById('disk_rate_1'));
      let mem_myChart = Vue.echarts.init(document.getElementById('mem_rate_1'));
      cpu_myChart.setOption({
    title : {
        text: '大数据类主机的cpu使用率分布',
        subtext: '资源分布占比',
        x:'center'
    },
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}% 台)"
    },
    legend: {
        orient: 'vertical',
        left: 'left',
        data: data.title[2]
    },
    series : [
        {
            name: 'cpu资源',
            type: 'pie',
            radius : '55%',
            center: ['50%', '60%'],
            data:data.data[2],
            itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
});
      disk_myChart.setOption({
    title : {
        text: '大数据类主机的磁盘使用率分布',
        subtext: '资源分布占比',
        x:'center'
    },
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}% 台)"
    },
    legend: {
        orient: 'vertical',
        left: 'left',
        data: data.title[1]
    },
    series : [
        {
            name: '磁盘资源',
            type: 'pie',
            radius : '55%',
            center: ['50%', '60%'],
            data:data.data[1],
            itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
});
      mem_myChart.setOption({
    title : {
        text: '大数据类主机的内存使用率分布',
        subtext: '资源分布占比',
        x:'center'
    },
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}% 台)"
    },
    legend: {
        orient: 'vertical',
        left: 'left',
        data: data.title[0]
    },
    series : [
        {
            name: '内存资源',
            type: 'pie',
            radius : '55%',
            center: ['50%', '60%'],
            data:data.data[0],
            itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
});
    })
  },
};


export default {
  state,
  actions,
  mutations
}
