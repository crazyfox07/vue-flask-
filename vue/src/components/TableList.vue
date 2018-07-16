<template>
<div>
  <el-table
    :data="tableData"
    stripe
    height="600"
    border
    align="left"
    style="width: 80%">
    <el-table-column
      fixed
      prop="date"
      label="日期"
      width="180">
    </el-table-column>
    <el-table-column
      prop="ip"
      label="IP"
      width="360">
    </el-table-column>
    <el-table-column
      prop="port"
      label="端口">
    </el-table-column>
  </el-table>

  <el-pagination
    background
    @current-change="queryPhoneTag"
    :current-page.sync="currentPage"
    layout="prev, pager, next"
    :total="100">
  </el-pagination>

  <el-row>
    <el-button type="success" v-on:click="queryPhoneTag">成功按钮</el-button>
  </el-row>
</div>
</template>

<script>
  import axios from 'axios'

  export default {
    data() {
      return {
        tableData: [],
        currentPage: 1,
      }
    },
    mounted: function(){
      this.getRequest();
    },
    methods:{
      getRequest:function(){
        axios.get('http://99.48.58.94:5000/',{
          params:{
            pageNo: this.currentPage
          }
        }).then((response) => {
          this.tableData.splice(0,this.tableData.length); // 先清空列表
          let items = response.data.result
          for(let item of items){
            this.tableData.push({
              'date':item['date'],
              'ip':item.ip,
              'port':item['port']
            })
          }
        }).catch(error => {
          console.log(error.response)
        });
      },

      queryPhoneTag: function (event) {
        this.getRequest()
      }
    }
  }
</script>
