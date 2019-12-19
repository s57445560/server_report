<template>

  <el-row v-if="report_status" style="position: absolute;top:60px;bottom: 0;left:200px;right: 0;overflow-x:hidden;overflow-y:auto;padding-top: 20px;">
    <el-row :gutter="12">
      <el-col :span="8">
        <el-card shadow="always">
          <i class="el-icon-s-platform"></i>服务器总数量：{{get_ip.servertotalcount}}
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card shadow="always">
          <i class="el-icon-s-platform"></i>物理机数量：{{get_ip.phycount}}
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card shadow="always">
          <i class="el-icon-s-platform"></i>虚拟机数量：{{get_ip.vircount}}
        </el-card>
      </el-col>
    </el-row>
      <el-col style="padding-top: 15px;">
        <el-tabs type="border-card" v-loading="get_loading">
          <el-tab-pane :label="title_list">
            <el-row style="padding-bottom: 8px;">
                <el-col :span="8">
                    <div class="block">
                    <span class="demonstration">选择查看日期</span>
                    <el-date-picker
                      v-model="Time"
                      align="right"
                      type="date"
                      value-format="yyyy-MM-dd"
                      placeholder="选择日期"
                      :picker-options="pickerOptions">
                    </el-date-picker>
                  </div>
                </el-col>
                <el-col :span="4">
                  <el-button type="primary" icon="el-icon-search" @click="filter_time">搜索</el-button>
                </el-col>
                <el-col :span="4">
                  <el-button type="primary" icon="el-icon-download" @click="download" :loading="get_b_loading">生成报表</el-button>
                </el-col>
                <el-col :span="5" :offset="3">
                  <div align="center">
                    <el-button type="text" @click="table = true">查看服务器详情</el-button>
                  </div>
                </el-col>
              </el-row>
<!--            内存的行-->
            <el-divider content-position="left">
              <span style="font-size: 20px;color: #409EFF;font-weight: bold"><i class="el-icon-data-line"></i> 内存</span>
            </el-divider>
            <el-row :gutter="5">
              <el-col :span="10" style="padding-bottom: 8px">
                <el-row :gutter="2">
                  <el-col :span="12">
                    <el-card class="box-card" style="height: 182px;">
                  <el-alert
                      title="应用内存使用情况"
                      type="success"
                      effect="dark"
                      center
                      :closable="false">
                    </el-alert>
                    <el-col :span="12" style="padding-top: 25px;">
                      <div align="center">
                        <el-tag type="info">
                            总量M
                          </el-tag>
                      </div>
                    </el-col>
                  <el-col :span="12" style="padding-top: 25px;">
                      <div align="center">
                        <el-tag type="info">
                            使用量M
                          </el-tag>
                      </div>
                    </el-col>

                  <el-col :span="12" style="padding-top: 8px;padding-bottom: 8px;">
                      <div align="center">
                        <el-tag type="">
                            {{get_all.all.service.memorytotal}}
                          </el-tag>
                      </div>
                    </el-col>
                  <el-col :span="12" style="padding-top: 8px;padding-bottom: 8px;">
                      <div align="center">
                        <el-tag type="">
                            {{get_all.all.service.memoryuse}}
                          </el-tag>
                      </div>
                    </el-col>
                </el-card>
                  </el-col>
                  <el-col :span="12">
                    <el-card class="box-card" style="height: 182px;">
                  <el-alert
                      title="大数据内存使用情况"
                      type="success"
                      center
                      effect="dark"
                      :closable="false">
                    </el-alert>
                    <el-col :span="12" style="padding-top: 25px;">
                      <div align="center">
                        <el-tag type="info">
                            总量M
                          </el-tag>
                      </div>
                    </el-col>
                  <el-col :span="12" style="padding-top: 25px;">
                      <div align="center">
                        <el-tag type="info">
                            使用量M
                          </el-tag>
                      </div>
                    </el-col>

                  <el-col :span="12" style="padding-top: 8px;padding-bottom: 8px;">
                      <div align="center">
                        <el-tag type="">
                            {{get_all.all.bigdata.memorytotal}}
                          </el-tag>
                      </div>
                    </el-col>
                  <el-col :span="12" style="padding-top: 8px;padding-bottom: 8px;">
                      <div align="center">
                        <el-tag type="">
                            {{get_all.all.bigdata.memoryuse}}
                          </el-tag>
                      </div>
                    </el-col>
                </el-card>
                  </el-col>
                </el-row>
                <el-row :gutter="2">
                  <el-col :span="12">
                    <el-card class="box-card">
                  <el-alert
                      title="应用内存使用率"
                      type="success"
                      center
                      effect="dark"
                      :closable="false">
                    </el-alert>
                  <div align="center" style="padding-top: 8px;">
                    <el-progress type="dashboard" :percentage="get_all.all.service.memoryrate|number" :color="colors"></el-progress>
                  </div>
                </el-card>
                  </el-col>
                  <el-col :span="12">
                    <el-card class="box-card">
                  <el-alert
                      title="大数据内存使用率"
                      type="success"
                      center
                      effect="dark"
                      :closable="false">
                    </el-alert>
                  <div align="center" style="padding-top: 8px;">
                    <el-progress type="dashboard" :percentage="get_all.all.bigdata.memoryrate|number" :color="colors"></el-progress>
                  </div>
                </el-card>
                  </el-col>
                </el-row>
              </el-col>
              <el-col :span="14">
                <el-card class="box-card" style="height: 397px;">
                  <div id="memory" style="height: 397px;"></div>
                </el-card>
              </el-col>
            </el-row>

            <el-row :gutter="5" style="padding-bottom: 8px;">
              <el-col :span="12">
                <el-card class="box-card" style="height: 397px;">
                      <div id="mem_rate_0" style="height: 397px;"></div>
                </el-card>
              </el-col>
              <el-col :span="12">
                <el-card class="box-card" style="height: 397px;">
                      <div id="mem_rate_1" style="height: 397px;"></div>
                </el-card>
              </el-col>
            </el-row>

            <el-row :gutter="5" style="padding-bottom: 10px;">
              <el-card class="box-card" style="height: 415px;">
                <div id="mem_all" style="height: 397px;"></div>
              </el-card>
            </el-row>

<!--            磁盘的行-->
            <el-divider content-position="left">
              <span style="font-size: 20px;color: #409EFF;font-weight: bold"><i class="el-icon-data-line"></i> 磁盘</span>
            </el-divider>
            <el-row :gutter="5">
              <el-col :span="10" style="padding-bottom: 8px">
                <el-row :gutter="2">
                  <el-col :span="12">
                    <el-card class="box-card" style="height: 182px;">
                  <el-alert
                      title="应用磁盘使用情况"
                      type="success"
                      center
                      effect="dark"
                      :closable="false">
                    </el-alert>
                    <el-col :span="12" style="padding-top: 25px;">
                      <div align="center">
                        <el-tag type="info">
                            总量G
                          </el-tag>
                      </div>
                    </el-col>
                  <el-col :span="12" style="padding-top: 25px;">
                      <div align="center">
                        <el-tag type="info">
                            使用量G
                          </el-tag>
                      </div>
                    </el-col>

                  <el-col :span="12" style="padding-top: 8px;padding-bottom: 8px;">
                      <div align="center">
                        <el-tag type="">
                            {{get_all.all.service.disktotal}}
                          </el-tag>
                      </div>
                    </el-col>
                  <el-col :span="12" style="padding-top: 8px;padding-bottom: 8px;">
                      <div align="center">
                        <el-tag type="">
                            {{get_all.all.service.diskuse}}
                          </el-tag>
                      </div>
                    </el-col>
                </el-card>
                  </el-col>
                  <el-col :span="12">
                    <el-card class="box-card" style="height: 182px;">
                  <el-alert
                      title="大数据磁盘使用情况"
                      type="success"
                      center
                      effect="dark"
                      :closable="false">
                    </el-alert>
                    <el-col :span="12" style="padding-top: 25px;">
                      <div align="center">
                        <el-tag type="info">
                            总量G
                          </el-tag>
                      </div>
                    </el-col>
                  <el-col :span="12" style="padding-top: 25px;">
                      <div align="center">
                        <el-tag type="info">
                            使用量G
                          </el-tag>
                      </div>
                    </el-col>

                  <el-col :span="12" style="padding-top: 8px;padding-bottom: 8px;">
                      <div align="center">
                        <el-tag type="">
                            {{get_all.all.bigdata.disktotal}}
                          </el-tag>
                      </div>
                    </el-col>
                  <el-col :span="12" style="padding-top: 8px;padding-bottom: 8px;">
                      <div align="center">
                        <el-tag type="">
                            {{get_all.all.bigdata.diskuse}}
                          </el-tag>
                      </div>
                    </el-col>
                </el-card>
                  </el-col>
                </el-row>
                <el-row :gutter="2">
                  <el-col :span="12">
                       <el-card class="box-card">
                          <el-alert
                          title="应用磁盘使用率"
                          type="success"
                          center
                          effect="dark"
                          :closable="false">
                        </el-alert>
                        <div align="center" style="padding-top: 8px;">
                          <el-progress type="dashboard" :percentage="get_all.all.service.diskrate|number" :color="colors"></el-progress>
                        </div>
                    </el-card>
                  </el-col>
                  <el-col :span="12">
                     <el-card class="box-card">
                        <el-alert
                        title="大数据磁盘使用率"
                        type="success"
                        center
                        effect="dark"
                        :closable="false">
                      </el-alert>
                      <div align="center" style="padding-top: 8px;">
                        <el-progress type="dashboard" :percentage="get_all.all.bigdata.diskrate|number" :color="colors"></el-progress>
                      </div>
                  </el-card>
                  </el-col>
                </el-row>
              </el-col>
              <el-col :span="14">
                <el-card class="box-card" style="height: 397px;">
                  <div id="disk" style="height: 397px;"></div>
                </el-card>
              </el-col>
            </el-row>

            <el-row :gutter="5" style="padding-bottom: 10px;">
              <el-col :span="12">
                <el-card class="box-card" style="height: 397px;">
                      <div id="disk_rate_0" style="height: 397px;"></div>
                </el-card>
              </el-col>
              <el-col :span="12">
                <el-card class="box-card" style="height: 397px;">
                      <div id="disk_rate_1" style="height: 397px;"></div>
                </el-card>
              </el-col>
            </el-row>

            <el-row :gutter="5" style="padding-bottom: 10px;padding-top: 8px;">
              <el-card class="box-card" style="height: 415px;">
                <div id="disk_all" style="height: 397px;"></div>
              </el-card>
            </el-row>

<!--            cpu的行-->
            <el-divider content-position="left">
              <span style="font-size: 20px;color: #409EFF;font-weight: bold"><i class="el-icon-data-line"></i> cpu</span>
            </el-divider>
            <el-row :gutter="5">
              <el-col :span="10" style="padding-bottom: 8px">
                <el-row :gutter="2">
                  <el-col :span="12">
                    <el-card class="box-card" style="height: 182px;">
                    <el-alert
                        title="应用cpu核数"
                        type="success"
                        center
                        effect="dark"
                        :closable="false">
                      </el-alert>
                    <el-col style="padding-top: 25px;">
                      <div align="center">
                        <el-tag type="info">
                            总核数
                          </el-tag>
                      </div>
                    </el-col>
                  <el-col style="padding-top: 8px;padding-bottom: 8px;">
                      <div align="center">
                        <el-tag type="">
                            {{get_all.all.service.cpucore}}
                          </el-tag>
                      </div>
                    </el-col>
                </el-card>
                  </el-col>
                  <el-col :span="12">
                    <el-card class="box-card" style="height: 182px;">
                  <el-alert
                      title="大数据cpu核数"
                      type="success"
                      center
                      effect="dark"
                      :closable="false">
                    </el-alert>
                    <el-col style="padding-top: 25px;">
                      <div align="center">
                        <el-tag type="info">
                            总核数
                          </el-tag>
                      </div>
                    </el-col>

                  <el-col style="padding-top: 8px;padding-bottom: 8px;">
                      <div align="center">
                        <el-tag type="">
                            {{get_all.all.bigdata.cpucore}}
                          </el-tag>
                      </div>
                    </el-col>
                </el-card>
                  </el-col>
                </el-row>
                <el-row :gutter="2">
                  <el-col :span="12">
                       <el-card class="box-card">
                          <el-alert
                          title="应用cpu使用率"
                          type="success"
                          center
                          effect="dark"
                          :closable="false">
                        </el-alert>
                        <div align="center" style="padding-top: 8px;">
                          <el-progress type="dashboard" :percentage="get_all.all.service.cpurate|number" :color="colors"></el-progress>
                        </div>
                    </el-card>
                  </el-col>
                  <el-col :span="12">
                     <el-card class="box-card">
                        <el-alert
                        title="大数据cpu使用率"
                        type="success"
                        center
                        effect="dark"
                        :closable="false">
                      </el-alert>
                      <div align="center" style="padding-top: 8px;">
                        <el-progress type="dashboard" :percentage="get_all.all.bigdata.cpurate|number" :color="colors"></el-progress>
                      </div>
                  </el-card>
                  </el-col>
                </el-row>
              </el-col>
              <el-col :span="14">
                <el-card class="box-card" style="height: 397px;">
                  <div id="cpu_table" style="height: 397px;"></div>
                </el-card>
              </el-col>
            </el-row>

            <el-row :gutter="5">
              <el-col :span="12">
                <el-card class="box-card" style="height: 397px;">
                      <div id="cpu_rate_0" style="height: 397px;"></div>
                </el-card>
              </el-col>
              <el-col :span="12">
                <el-card class="box-card" style="height: 397px;">
                      <div id="cpu_rate_1" style="height: 397px;"></div>
                </el-card>
              </el-col>
            </el-row>

            <el-row :gutter="5" style="padding-bottom: 10px;padding-top: 8px;">
              <el-card class="box-card" style="height: 415px;">
                <div id="cpu_all" style="height: 397px;"></div>
              </el-card>
            </el-row>


          </el-tab-pane>
        </el-tabs>
      </el-col>
    <el-drawer
      title="服务器详情!"
      :visible.sync="table"
      direction="rtl"
      size="89%"
      >
      <el-row>
        <el-col style="padding-left: 20px;">
            <el-form :inline="true" :model="filter_ip" class="demo-form-inline" @submit.native.prevent>
              <el-form-item label="审批人">
                <el-input v-model="filter_ip.ip" placeholder="搜索ip" @keyup.enter.native="onSubmit()"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="onSubmit" >查询</el-button>
              </el-form-item>
            </el-form>
          </el-col>
      </el-row>
       <el-table :data="get_ip.IP" stripe border size="mini" v-loading="get_loading" @sort-change="check_sort" @filter-change="filterType">
          <el-table-column property="name" label="IP" width="120"></el-table-column>
          <el-table-column property="memorytotal" label="内存总量/M"></el-table-column>
          <el-table-column property="memoryuse" label="内存使用量/M"></el-table-column>
          <el-table-column property="memoryrate" label="内存使用率" :formatter="filter_m_rate" sortable="custom"></el-table-column>
          <el-table-column property="cpucore" label="cpu核数"></el-table-column>
          <el-table-column property="averageload" label="平均load"></el-table-column>
          <el-table-column property="cpurate" label="cpu使用率" :formatter="filter_c_rate" sortable="custom"></el-table-column>
          <el-table-column property="disktotal" label="磁盘总量/G"></el-table-column>
          <el-table-column property="diskuse" label="磁盘使用量/G"></el-table-column>
          <el-table-column property="diskrate" label="磁盘使用率" :formatter="filter_d_rate" sortable="custom"></el-table-column>
          <el-table-column property="servertype" label="服务器类型"></el-table-column>
          <el-table-column property="type" label="所属环境" :formatter="filterTag"
                           :filters="[{ text: '应用', value: 'service' }, { text: '大数据', value: 'big_data' }]"
                            column-key="type"
          ></el-table-column>
        </el-table>
      <div align="center" style="padding-top: 8px;">
        <el-pagination
          @current-change="handleCurrentChange"
          background
          layout="prev, pager, next"
          :total="get_ip.select_number">
        </el-pagination>
      </div>
    </el-drawer>

    </el-row>

</template>

<script>
export default {
  name: 'report',
  data () {
    return {
      msg: '报表服务',
      drawer:false,
      pickerOptions: {
        disabledDate(time) {
          return time.getTime() > Date.now();
        }
      },
      select:'',
      Time: '',
      report_status:true,
      colors: [
        {color: '#6f7ad3', percentage: 20},
        {color: '#1989fa', percentage: 40},
        {color: '#5cb87a', percentage: 60},
        {color: '#e6a23c', percentage: 80},
        {color: '#f56c6c', percentage: 100}
      ],
      table: false,
      dialog: false,
      loading: false,
      order: '',
      filter_ip: {}
    }
  },
  methods:{
    filterTag(row, column) {
        if(row.type === 'service'){
          return "应用"
        }
        return "大数据";
      },
    filterType(value) {
      console.log("紧来了",value.type);
        if(value.type[0] === "service"){
          this.select = 0;
        }else if(value.type[0] === "big_data"){
          this.select = 1;
        }else{
          this.select = ''
        }
        var Json_data = this.$cookies.get("Title").split("/");
        this.$store.dispatch('get_ip_list',{"b":Json_data[0],"e":Json_data[1],"timestrap":this.Time,'order':this.order,"filter":this.filter_ip.ip,"select":this.select});
        return true

      },
    onSubmit() {
        console.log('submit!');
        var Json_data = this.$cookies.get("Title").split("/");
        this.$store.dispatch('get_ip_list',{"b":Json_data[0],"e":Json_data[1],"timestrap":this.Time,'order':this.order,"filter":this.filter_ip.ip,"select":this.select});
      },
    download(){
      this.$store.dispatch('download',{"timestrap":this.Time});
    },
    check_sort(name,status,order){
      console.log(name,status,order);
      let id = name.prop;
      let s = name.order;
      if(s === null){
        this.order = ''
      }else if (s === "descending"){
        this.order = id
      }else if(s === "ascending"){
        this.order = "-"+id
      }
      console.log(this.order);
      var Json_data = this.$cookies.get("Title").split("/");
      this.$store.dispatch('get_ip_list',{"b":Json_data[0],"e":Json_data[1],"timestrap":this.Time,'order':this.order,"filter":this.filter_ip.ip,"select":this.select});
    },
    filter_time(){
      var Json_data = this.$cookies.get("Title").split("/");
      this.$store.dispatch('get_ip_list',{"b":Json_data[0],"e":Json_data[1],"timestrap":this.Time});
      this.$store.dispatch('get_all_list',{"b":Json_data[0],"e":Json_data[1],"timestrap":this.Time});
      this.$store.dispatch('get_memory',{"b":Json_data[0],"e":Json_data[1],"timestrap":this.Time});
      this.$store.dispatch('get_disk',{"b":Json_data[0],"e":Json_data[1],"timestrap":this.Time});
      this.$store.dispatch('get_cpu',{"b":Json_data[0],"e":Json_data[1],"timestrap":this.Time});
    },
    filter_m_rate(row,column){
      return row.memoryrate + "%"
    },
    filter_d_rate(row,column){
      return row.diskrate + "%"
    },
    filter_c_rate(row,column){
      if(row.cpurate === ""){
        return "0.00%"
      }
      return row.cpurate + "%"
    },
      handleCurrentChange(val) {
        console.log(`当前页: ${val}`);
        var Json_data = this.$cookies.get("Title").split("/");
        this.$store.dispatch('get_ip_list',{"b":Json_data[0],"e":Json_data[1],'page':val,"timestrap":this.Time,'order':this.order,"filter":this.filter_ip.ip,"select":this.select});
      }
  },
  computed:{
      title_list(){
          return this.$store.state.Base.Title;
      },
      get_ip(){
        return this.$store.state.Base.Ip;
      },
      get_loading(){
        return this.$store.state.Base.loading;
      },
    get_b_loading(){
        return this.$store.state.Base.b_loading;
      },
      get_all(){
        return this.$store.state.Base.All;
      },
      get_report_status(){
        return this.$store.state.Base.report_status;
      },
    get_title(){
        return this.$store.state.Base.Title;
      }
  },
  created(){
      var Json_data = this.$cookies.get("Title").split("/");
      this.$store.dispatch('get_ip_list',{"b":Json_data[0],"e":Json_data[1]});
      this.$store.dispatch('get_all_list',{"b":Json_data[0],"e":Json_data[1]});
      this.$store.dispatch('get_memory',{"b":Json_data[0],"e":Json_data[1],"timestrap":this.Time});
      this.$store.dispatch('get_disk',{"b":Json_data[0],"e":Json_data[1],"timestrap":this.Time});
      this.$store.dispatch('get_cpu',{"b":Json_data[0],"e":Json_data[1],"timestrap":this.Time});
      this.$store.dispatch('get_rate_0',{"b":Json_data[0],"e":Json_data[1],"timestrap":this.Time,'type':0});
      this.$store.dispatch('get_rate_1',{"b":Json_data[0],"e":Json_data[1],"timestrap":this.Time,'type':1});
      this.$store.dispatch('get_all',{"b":Json_data[0],"e":Json_data[1]});
      if(this.$cookies.isKey("Title")){
        this.$store.commit("set_title",this.$cookies.get("Title"))
      }
      this.filter_ip = {};
      this.order = ''
  },
     watch:{
         get_title(){
           this.filter_ip = {};
            console.log("watch 变化了");
              this.report_status = false;
              this.$nextTick(()=>{
                this.report_status = true
            })
        }
   }
}
</script>


<style scoped>

</style>
