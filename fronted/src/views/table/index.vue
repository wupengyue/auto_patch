<template>
  <div class="app-container">
    <el-table
      v-loading="listLoading"
      :data="list"
      element-loading-text="Loading"
      border
      fit
      highlight-current-row
    >
      <el-table-column align="center" label="CASE ID" width="95">
        <template slot-scope="scope">
          {{ scope.row.case_id }}
        </template>
      </el-table-column>
      <el-table-column label="CaseName">
        <template slot-scope="scope">
          {{ scope.row.case_name }}
        </template>
      </el-table-column>
      <el-table-column label="Case Number" width="110" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.case_serial_number }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Case Sign" width="110" align="center">
        <template slot-scope="scope">
          {{ scope.row.case_sign }}
        </template>
      </el-table-column>
      <el-table-column class-name="status-col" label="Case Type" width="110" align="center">
        <template slot-scope="scope">
          <el-tag :type="scope.row.status | statusFilter">{{ scope.row.case_type }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column align="center" prop="created_at" label="Cteate Time" width="200">
        <template slot-scope="scope">
          <i class="el-icon-time"/>
          <span>{{ scope.row.create_time }}</span>
        </template>
      </el-table-column>
      <el-table-column align="center" prop="created_at" label="Update Time" width="200">
        <template slot-scope="scope">
          <i class="el-icon-time"/>
          <span>{{ scope.row.update_time }}</span>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { getList } from '@/api/table'

export default {
  filters: {
    statusFilter(status) {
      const statusMap = {
        published: 'success',
        draft: 'gray',
        deleted: 'danger'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      list: null,
      listLoading: true
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.listLoading = true
      getList().then(response => {
        this.list = response.data
        this.listLoading = false
      })
    }
  }
}
</script>
