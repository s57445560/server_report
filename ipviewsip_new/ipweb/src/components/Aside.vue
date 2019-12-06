<template>
    <div>
        <el-menu background-color="#545c64"
                 :default-active="Index"
                 text-color="#fff"
                 active-text-color="#ffd04b"
                 @open="handleOpen"
                 @close="handleClose"
                 unique-opened
                 style="position: absolute;bottom: 0;top:60px;width: 200px;left: 0px;"
                 align="left">
            <el-menu-item index="/" @click="home()">
                    <i class="el-icon-menu"></i>
                    <span slot="title">首页信息</span>
            </el-menu-item>

            <el-submenu v-for="(v,k) in base_list" :index="v.name" :key="k">
                <template slot="title"><i class="el-icon-setting"></i>{{v.name}}</template>
                <el-menu-item-group v-for="(vv,kk) in v.e_list" :key="kk">
                        <el-menu-item  :index="vv[0]" v-on:click="show(vv[1],vv[0],v.name)">{{vv[1]}}</el-menu-item>
                </el-menu-item-group>

            </el-submenu>
        </el-menu>
    </div>
</template>

<script>
    import ElCol from "element-ui/packages/col/src/col";
    export default {
        components: {ElCol},
        name: 'el-aside',
        data () {
            return {
                url:'5',
                status:0
            }
        },
        methods: {
          handleOpen(key, keyPath) {
            this.status = key;
          },
          handleClose(key, keyPath) {
            console.log(key, keyPath);
          },
          show(ename,id,bname){
            this.$router.push({"path":'/report'});
            // this.url = this.status;
            this.$store.dispatch('get_ip_list',{"e":ename,"b":bname,'id':id});
            this.$store.dispatch('get_all_list',{"e":ename,"b":bname,'id':id});
            this.$store.dispatch('get_memory',{"e":ename,"b":bname,'id':id});
            this.$store.dispatch('get_disk',{"e":ename,"b":bname,'id':id});
            this.$store.dispatch('get_cpu',{"e":ename,"b":bname,'id':id});
            this.$store.dispatch('get_rate_0',{"e":ename,"b":bname,'id':id,"timestrap":this.Time,'type':0});
            this.$store.dispatch('get_rate_1',{"e":ename,"b":bname,'id':id,"timestrap":this.Time,'type':1});

          },
          home(){
            this.$router.push({"path":'/'});
            this.$store.dispatch("get_home");
          }
        },

      computed:{
            base_list(){

                return this.$store.state.Base.tableData;
            },
            Index(){
              return this.$store.state.Base.ID;
            },
        },
      created(){
            this.url =  this.$route.path;
            this.$store.dispatch('base_list');
            // var Json_data = this.$cookies.get("Title").split("/");

            // this.$store.dispatch('get_ip_list',{"b":Json_data[0],"e":Json_data[1]});
            // this.$store.dispatch('get_all_list',{"b":Json_data[0],"e":Json_data[1]});

            if(this.$route.path === '/'){
              this.$store.commit("set_id",'/')
            }else {
              if (this.$cookies.isKey("ID")) {
                this.$store.commit("set_id", this.$cookies.get("ID"))
              }
            }
        },
    }
</script>


<style scoped>
a {
    text-decoraction: none;
}
li {
  align: left;
}
.router-link-active {
    text-decoration: none;
}
</style>
