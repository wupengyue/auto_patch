<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.case_id" placeholder="JIRA ID" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-select v-model="listQuery.case_type" placeholder="Case Type" clearable style="width: 130px; margin-left: 10px;" class="filter-item">
        <el-option v-for="item in caseTypeOptions" :key="item" :label="item" :value="item" />
      </el-select>
      <el-button v-waves class="filter-item" type="primary" style="margin-left: 10px;" icon="el-icon-search" @click="handleFilter">
        Search
      </el-button>
      <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreate">
        Add
      </el-button>
    </div>
    <p></p>

    <el-table :key="tableKey" v-loading="listLoading" :data="list" border fit highlight-current-row style="width: 100%;">
      <el-table-column label="CASE ID" prop="id" sortable="custom" align="center" width="110">
        <template v-slot="{row}">
          <span>{{ row.case_id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Case Name" min-width="150px">
        <template v-slot="{row}">
          {{ row.case_name }}
        </template>
      </el-table-column>
      <el-table-column label="Case Number" width="120px" align="center">
        <template v-slot="{row}">
          <span>{{ row.case_serial_number }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Case Sign" width="110px">
        <template v-slot="{row}">
          {{ row.case_sign }}
        </template>
      </el-table-column>
      <el-table-column label="Case Type" align="center" width="95">
        <template v-slot="{row}">
          {{ row.case_type }}
        </template>
      </el-table-column>
      <el-table-column label="Create At" width="160px" align="center">
        <template v-slot="{row}">
          <span>{{ row.create_time }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Update At" width="160px" align="center">
        <template v-slot="{row}">
          <span>{{ row.update_time }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Actions" align="center" width="200" class-name="small-padding fixed-width">
        <template v-slot="{row,$index}">
          <el-button type="primary" size="mini" @click="handleUpdate(row)">
            Edit
          </el-button>
          <el-button v-if="row.status!='deleted'" size="mini" type="danger" @click="handleDelete(row,$index)">
            Delete
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList"/>

    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :rules="rules" :model="temp" label-position="left" label-width="120px" style="width: 400px; margin-left:50px;">
        <el-form-item label="Case ID" prop="case_id">
          <el-input v-model="temp.case_id" />
        </el-form-item>
        <el-form-item label="Case Name" prop="case_name">
          <el-input v-model="temp.case_name" />
        </el-form-item>
        <el-form-item label="Case Number" prop="case_serial_number">
          <el-input v-model="temp.case_serial_number" />
        </el-form-item>
        <el-form-item label="Case Sign" prop="case_sign">
          <el-input v-model="temp.case_sign" />
        </el-form-item>
        <el-form-item label="Type" prop="case_type">
          <el-select v-model="temp.case_type" class="filter-item" placeholder="Please select">
            <el-option v-for="item in caseTypeOptions" :key="item" :label="item" :value="item" />
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">
          Cancel
        </el-button>
        <el-button type="primary" @click="dialogStatus==='create'?createData():updateData()">
          Confirm
        </el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { fetchList, createProjectCase, updateProjectCase } from '@/api/table'
import waves from '@/directive/waves' // waves directive
import Pagination from '@/components/Pagination'
export default {
  name: 'ComplexTable',
  components: { Pagination },
  directives: { waves },
  data() {
    return {
      tableKey: 0,
      list: null,
      total: 0,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 20,
        case_id: undefined,
        case_type: undefined
      },
      caseTypeOptions: [0, 1, 2, 3],
      sortOptions: [{ label: 'ID Ascending', key: '+id' }, { label: 'ID Descending', key: '-id' }],
      statusOptions: ['published', 'draft', 'deleted'],
      temp: {
        case_id: '',
        case_type: '',
        status: '',
        case_name: '',
        case_serial_number: '',
        case_sign: ''
      },
      dialogFormVisible: false,
      dialogStatus: '',
      textMap: {
        update: 'Edit',
        create: 'Create'
      },
      pvData: [],
      rules: {
        type: [{ required: true, message: 'type is required', trigger: 'change' }],
        timestamp: [{ type: 'date', required: true, message: 'timestamp is required', trigger: 'change' }],
        title: [{ required: true, message: 'title is required', trigger: 'blur' }]
      },
      downloadLoading: false
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      fetchList(this.listQuery).then(response => {
        this.list = response.data
        this.total = response.total
        this.listLoading = false
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      this.getList()
    },
    resetTemp() {
      this.temp = {
        title: '',
        type: '',
        case_id: '',
        case_type: '',
        status: '',
        case_name: '',
        case_serial_number: '',
        case_sign: ''
      }
    },
    handleCreate() {
      this.resetTemp()
      this.dialogStatus = 'create'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          this.temp.id = parseInt(Math.random() * 100) + 1024 // mock a id
          this.temp.author = 'vue-element-admin'
          createProjectCase(this.temp).then(() => {
            this.list.unshift(this.temp)
            this.dialogFormVisible = false
            this.$notify({
              title: 'Success',
              message: 'Created Successfully',
              type: 'success',
              duration: 2000
            })
          })
        }
      })
    },
    handleUpdate(row) {
      this.temp = Object.assign({}, row) // copy obj
      this.temp.timestamp = new Date(this.temp.timestamp)
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.temp)
          updateProjectCase(tempData).then(() => {
            const index = this.list.findIndex(v => v.id === this.temp.id)
            this.list.splice(index, 1, this.temp)
            this.dialogFormVisible = false
            this.$notify({
              title: 'Success',
              message: 'Update Successfully',
              type: 'success',
              duration: 2000
            })
          })
        }
      })
    },
    handleDelete(row, index) {
      this.$notify({
        title: 'Success',
        message: 'Delete Successfully',
        type: 'success',
        duration: 2000
      })
      this.list.splice(index, 1)
    }
  }
}

</script>
