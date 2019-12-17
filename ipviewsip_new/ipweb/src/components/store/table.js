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

  get_all({state, commit, rootState},data){
    Vue.http.get(Vue.baseConfig.request_url + "/api/v1/resource_curve", {
      params: data
    }).then(function (resp) {
      var data = resp.data;
      console.log(data);
      let mem_all = Vue.echarts.init(document.getElementById('mem_all'));
      let disk_all = Vue.echarts.init(document.getElementById('disk_all'));
      let cpu_all = Vue.echarts.init(document.getElementById('cpu_all'));
      mem_all.setOption({
    title: {
        text: '内存使用率历史图'
    },
    color:['#88cb7e','#6e79c2'],
    tooltip: {
        trigger: 'axis',
        formatter:function (params,ticket,callback) {
          var st = params[0]["axisValue"] + "<br/>";
          for(let v of params){
            st = st +"<span style=\" color:"+v["color"]["colorStops"][0]["color"]+"\">"+ v["seriesName"] + " : "+ v["data"]+"%" +"</span>"+ "<br/>"
          }
          return st
        }
    },
    legend: {
        data:data[0]
    },
    toolbox: {
        dataZoom: {
            yAxisIndex: 'none'  // y轴不缩放，Index默认为0
        },
        restore: {},
        saveAsImage: {}
    },
    dataZoom: [{                 // 内置于坐标系中，使用户可以在坐标系上通过鼠标拖拽、鼠标滚轮、手指滑动（触屏上）来缩放或漫游坐标系
        type: 'inside',
        start: 40,
        }, {
            start: 0,
            end: 0,                  // handleIcon 手柄的 icon 形状，支持路径字符串
            handleIcon: 'M10.7,11.9v-1.3H9.3v1.3c-4.9,0.3-8.8,4.4-8.8,9.4c0,5,3.9,9.1,8.8,9.4v1.3h1.3v-1.3c4.9-0.3,8.8-4.4,8.8-9.4C19.5,16.3,15.6,12.2,10.7,11.9z M13.3,24.4H6.7V23h6.6V24.4z M13.3,19.6H6.7v-1.4h6.6V19.6z',
            handleSize: '80%',        //  控制手柄的尺寸，可以是像素大小，也可以是相对于 dataZoom 组件宽度的百分比，默认跟 dataZoom 宽度相同。
            handleStyle: {
                color: 'pink',
                shadowBlur: 3,      // shadowBlur图片阴影模糊值，shadowColor阴影的颜色
                shadowColor: 'red',
                shadowOffsetX: 2,
                shadowOffsetY: 2
                }
            }],
    xAxis: {
        type: 'category',
        boundaryGap: false,
            axisLine: {//坐标轴
        lineStyle:{
            opacity: 0.00,//设置透明度就可以控制显示不显示
        },
    },
        data: data[1]
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        name:'应用内存',
        data: data[2],
        type: 'line',
        areaStyle: {},
        color: new Vue.echarts.graphic.LinearGradient(0, 0, 0, 1,[{
              offset: 0, color: '#ff9055' // 0% 处的颜色
             }, {
                 offset: 0.4, color: '#ff9055' // 100% 处的颜色
             }, {
                 offset: 1, color: '#fff' // 100% 处的颜色
             }]
         ),
    },
    {
        name:'大数据内存',
        data: data[3],
        type: 'line',
        areaStyle: {},
        color: new Vue.echarts.graphic.LinearGradient(0, 0, 0, 1,[{
              offset: 0, color: '#6ea695' // 0% 处的颜色
             }, {
                 offset: 0.4, color: '#6ea695' // 100% 处的颜色
             }, {
                 offset: 1, color: '#fff' // 100% 处的颜色
             }]
         ),
    }]
});
      disk_all.setOption({
    title: {
        text: '磁盘使用率历史图'
    },
    color:['#88cb7e','#6e79c2'],
    tooltip: {
        trigger: 'axis',
        formatter:function (params,ticket,callback) {
          var st = params[0]["axisValue"] + "<br/>";
          for(let v of params){
            st = st +"<span style=\" color:"+v["color"]["colorStops"][0]["color"]+"\">"+ v["seriesName"] + " : "+ v["data"]+"%" +"</span>"+ "<br/>"
          }
          return st
        }
    },
    legend: {
        data:data[0]
    },
    toolbox: {
        dataZoom: {
            yAxisIndex: 'none'  // y轴不缩放，Index默认为0
        },
        restore: {},
        saveAsImage: {}
    },
    dataZoom: [{                 // 内置于坐标系中，使用户可以在坐标系上通过鼠标拖拽、鼠标滚轮、手指滑动（触屏上）来缩放或漫游坐标系
        type: 'inside',
        start: 40,
        }, {
            start: 0,
            end: 0,                  // handleIcon 手柄的 icon 形状，支持路径字符串
            handleIcon: 'M10.7,11.9v-1.3H9.3v1.3c-4.9,0.3-8.8,4.4-8.8,9.4c0,5,3.9,9.1,8.8,9.4v1.3h1.3v-1.3c4.9-0.3,8.8-4.4,8.8-9.4C19.5,16.3,15.6,12.2,10.7,11.9z M13.3,24.4H6.7V23h6.6V24.4z M13.3,19.6H6.7v-1.4h6.6V19.6z',
            handleSize: '80%',        //  控制手柄的尺寸，可以是像素大小，也可以是相对于 dataZoom 组件宽度的百分比，默认跟 dataZoom 宽度相同。
            handleStyle: {
                color: 'pink',
                shadowBlur: 3,      // shadowBlur图片阴影模糊值，shadowColor阴影的颜色
                shadowColor: 'red',
                shadowOffsetX: 2,
                shadowOffsetY: 2
                }
            }],
    xAxis: {
        type: 'category',
        boundaryGap: false,
            axisLine: {//坐标轴
        lineStyle:{
            opacity: 0.00,//设置透明度就可以控制显示不显示
        },
    },
        data: data[1]
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        name:'应用磁盘',
        data: data[4],
        type: 'line',
        areaStyle: {},
        color: new Vue.echarts.graphic.LinearGradient(0, 0, 0, 1,[{
              offset: 0, color: '#ff9055' // 0% 处的颜色
             }, {
                 offset: 0.4, color: '#ff9055' // 100% 处的颜色
             }, {
                 offset: 1, color: '#fff' // 100% 处的颜色
             }]
         ),
    },
    {
        name:'大数据磁盘',
        data: data[5],
        type: 'line',
        areaStyle: {},
        color: new Vue.echarts.graphic.LinearGradient(0, 0, 0, 1,[{
              offset: 0, color: '#6ea695' // 0% 处的颜色
             }, {
                 offset: 0.4, color: '#6ea695' // 100% 处的颜色
             }, {
                 offset: 1, color: '#fff' // 100% 处的颜色
             }]
         ),
    }]
});
      cpu_all.setOption({
    title: {
        text: 'cpu使用率历史图'
    },
    color:['#88cb7e','#6e79c2'],
    tooltip: {
        trigger: 'axis',
        formatter:function (params,ticket,callback) {
          var st = params[0]["axisValue"] + "<br/>";
          for(let v of params){
            st = st +"<span style=\" color:"+v["color"]["colorStops"][0]["color"]+"\">"+ v["seriesName"] + " : "+ v["data"]+"%" +"</span>"+ "<br/>"
          }
          return st
        }
    },
    legend: {
        data:data[0]
    },
    toolbox: {
        dataZoom: {
            yAxisIndex: 'none'  // y轴不缩放，Index默认为0
        },
        restore: {},
        saveAsImage: {}
    },
    dataZoom: [{                 // 内置于坐标系中，使用户可以在坐标系上通过鼠标拖拽、鼠标滚轮、手指滑动（触屏上）来缩放或漫游坐标系
        type: 'inside',
        start: 40,
        }, {
            start: 0,
            end: 0,                  // handleIcon 手柄的 icon 形状，支持路径字符串
            handleIcon: 'M10.7,11.9v-1.3H9.3v1.3c-4.9,0.3-8.8,4.4-8.8,9.4c0,5,3.9,9.1,8.8,9.4v1.3h1.3v-1.3c4.9-0.3,8.8-4.4,8.8-9.4C19.5,16.3,15.6,12.2,10.7,11.9z M13.3,24.4H6.7V23h6.6V24.4z M13.3,19.6H6.7v-1.4h6.6V19.6z',
            handleSize: '80%',        //  控制手柄的尺寸，可以是像素大小，也可以是相对于 dataZoom 组件宽度的百分比，默认跟 dataZoom 宽度相同。
            handleStyle: {
                color: 'pink',
                shadowBlur: 3,      // shadowBlur图片阴影模糊值，shadowColor阴影的颜色
                shadowColor: 'red',
                shadowOffsetX: 2,
                shadowOffsetY: 2
                }
            }],
    xAxis: {
        type: 'category',
        boundaryGap: false,
            axisLine: {//坐标轴
        lineStyle:{
            opacity: 0.00,//设置透明度就可以控制显示不显示
        },
    },
        data: data[1]
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        name:'应用cpu',
        data: data[6],
        type: 'line',
        areaStyle: {},
        color: new Vue.echarts.graphic.LinearGradient(0, 0, 0, 1,[{
              offset: 0, color: '#ff9055' // 0% 处的颜色
             }, {
                 offset: 0.4, color: '#ff9055' // 100% 处的颜色
             }, {
                 offset: 1, color: '#fff' // 100% 处的颜色
             }]
         ),
    },
    {
        name:'大数据cpu',
        data: data[7],
        type: 'line',
        areaStyle: {},
        color: new Vue.echarts.graphic.LinearGradient(0, 0, 0, 1,[{
              offset: 0, color: '#6ea695' // 0% 处的颜色
             }, {
                 offset: 0.4, color: '#6ea695' // 100% 处的颜色
             }, {
                 offset: 1, color: '#fff' // 100% 处的颜色
             }]
         ),
    }]
});
    })
  },
};


export default {
  state,
  actions,
  mutations
}
