<template>
  <div class="author-basic">
    <div style="text-align:left;">
      <span class="author-name" >作者：{{ authorInfo.name }}</span>
    </div>
    <!-- <div style="text-align:left;margin-top:20px;">
      简介：<span class="abstract">{{ authorInfo.abstract|ellipsis }}</span>
    </div> -->
    <div style="padding-top:20px">
      <span class="latest-version">邮箱：{{ authorInfo.email }}</span>
    </div>
    <div style="padding-top:20px">
      <span class="latest-version">个人网站：{{ authorInfo.personal_site }}</span>
    </div>
    <div v-if="authorInfo.maintainer_overdue" style="padding-top:20px;color:#A0A0A0;font-size:16px">
      注意：该作者域名已过期！
    </div>
    <!-- <div id="network_id" class="network" style="padding-top:20px;height:70vh"></div>
      <el-dialog title="测试框" :visible.sync="dialogVisible" width="width">
        <div>参与项目</div>
        <div slot="footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
        </div>
      </el-dialog> -->
    </div>
</template>
  
  <script>
import Vis from "vis";
export default {
  name: "AuthorInfo",
  props: ["authorInfo"],
  filters: {
    ellipsis: function(value) {
      if(!value) return "";
      if(value.length > 68) {
        return value.slice(0, 68) + "...";
      }
      return value;
    },
  },
  data() {
    return {
      dialogVisible: false,
      nodes: [],
      edges: [],
      // network:null,
      container: null,
      //   节点数组
      nodesArray: [
        {
          id: 0,
          label: "",
          color: { background: "red" }
        },
        {
          id: 1,
          label: "",  
          url: "",
          color: { background: "pink" }
        },
        {
          id: 2,
          label: "",
          url: "",
          color: { background: "pink" }
        },
        {
          id: 3,
          label: "",
          url: "",
          color: { background: "pink" }
        },
        {
          id: 4,
          label: "",
          url: "",
          color: { background: "pink" }
        },
        {
          id: 5,
          label: "",
          url: "",
          color: { background: "pink" }
        },
        {
          id: 6,
          label: "",
          url: "",
          color: { background: "pink" }
        },
        {
          id: 7,
          label: "",
          url: "",
          color: { background: "pink" }
        },
        {
          id: 8,
          label: "",
          url: "",
          color: { background: "pink" }
        }
      ],
      //   关系线数组
      edgesArray: [
        { from: '', to: '', label: "" },
        { from: '', to: '', label: "" },
        { from: '', to: '', label: "" },
        { from: '', to: '', label: "" },
        { from: '', to: '', label: "" },
        { from: '', to: '', label: "" },
        { from: '', to: '', label: "" },
        { from: '', to: '', label: "" },
      ],
      options: {},
      data: {}
    };
  },
  methods: {
    init() {
      this.nodesArray.splice(this.authorInfo.projects_involved.length + 1, this.nodesArray.length - this.authorInfo.projects_involved.length);
      this.nodesArray[0].label = this.authorInfo.name;
      for(let i = 0; i < this.authorInfo.projects_involved.length; i++) {
        console.log(this.authorInfo.projects_involved[i].proName);
        this.nodesArray[i + 1].label = this.authorInfo.projects_involved[i].proName;
        if(this.nodesArray[i + 1].label.length > 10) {
          this.nodesArray[i + 1].label = this.authorInfo.projects_involved[i].proName.slice(0, 10)
        }
        this.nodesArray[i + 1].url = this.authorInfo.projects_involved[i].url;
        this.edgesArray[i].from = 0;
        this.edgesArray[i].to = i + 1;
        this.edgesArray[i].label = "involve"
      }
      let _this = this;
      //1.创建一个nodes数组
      _this.nodes = new Vis.DataSet(_this.nodesArray);
      //2.创建一个edges数组
      _this.edges = new Vis.DataSet(_this.edgesArray);
      _this.container = document.getElementById("network_id");
      _this.data = {
        nodes: _this.nodes,
        edges: _this.edges
      };
      _this.options = {
        autoResize: true, //网络将自动检测其容器的大小调整，并相应地重绘自身
        locale: "cn", //语言设置：工具栏显示中文
        //设置语言
        locales: {
          cn: {
            //工具栏
            edit: "edit",
            del: "删除当前节点或关系",
            back: "返回",
            addNode: "添加节点",
            addEdge: "添加连线",
            editNode: "编辑节点",
            editEdge: "编辑连线",
            addDescription: "点击空白处可添加节点",
            edgeDescription: "点击某个节点拖拽连线可连接另一个节点",
            editEdgeDescription: "可拖拽连线改变关系",
            createEdgeError: "无法将边连接到集群",
            deleteClusterError: "无法删除集群.",
            editClusterError: "无法编辑群集'"
          }
        },
 
        // 设置节点样式
        nodes: {
          shape: "circle",
          size: 50,
          font: {
            //字体配置
            size: 32
          },
          color: {
            // border: "#2B7CE9", //节点边框颜色
            background: "#97C2FC", //节点背景颜色
            highlight: {
              //节点选中时状态颜色
              border: "#2B7CE9",
              background: "#D2E5FF"
            },
            hover: {
              //节点鼠标滑过时状态颜色
              border: "#2B7CE9",
              background: "#D2E5FF"
            }
          },
          borderWidth: 0, //节点边框宽度，单位为px
          borderWidthSelected: 2 //节点被选中时边框的宽度，单位为px
        },
        // 边线配置
        edges: {
          width: 1,
          length: 260,
          color: {
            color: "#848484",
            highlight: "#848484",
            hover: "#848484",
            inherit: "from",
            opacity: 1.0
          },
          shadow: true,
          smooth: {
            //设置两个节点之前的连线的状态
            enabled: true //默认是true，设置为false之后，两个节点之前的连线始终为直线，不会出现贝塞尔曲线
          },
          arrows: { to: true } //箭头指向to
        },
        //计算节点之前斥力，进行自动排列的属性
        physics: {
          enabled: true, //默认是true，设置为false后，节点将不会自动改变，拖动谁谁动。不影响其他的节点
          barnesHut: {
            gravitationalConstant: -4000,
            centralGravity: 0.3,
            springLength: 120,
            springConstant: 0.04,
            damping: 0.09,
            avoidOverlap: 0
          }
        },
        //用于所有用户与网络的交互。处理鼠标和触摸事件以及导航按钮和弹出窗口
        interaction: {
          hover: true,
          dragNodes: true, //是否能拖动节点
          dragView: true, //是否能拖动画布
          hover: true, //鼠标移过后加粗该节点和连接线
          multiselect: true, //按 ctrl 多选
          selectable: true, //是否可以点击选择
          selectConnectedEdges: true, //选择节点后是否显示连接线
          hoverConnectedEdges: true, //鼠标滑动节点后是否显示连接线
          zoomView: true //是否能缩放画布
        },
        //操作模块:包括 添加、删除、获取选中点、设置选中点、拖拽系列、点击等等
        manipulation: {
          enabled: true, //该属性表示可以编辑，出现编辑操作按钮
          addNode: true,
          addEdge: true,
          // editNode: undefined,
          editEdge: true,
          deleteNode: true,
          deleteEdge: true
        }
      };
 
      _this.network = new Vis.Network(
        _this.container,
        _this.data,
        _this.options
      );
    },
 
    resetAllNodes() {
      let _this = this;
      _this.nodes.clear();
      _this.edges.clear();
      _this.nodes.add(_this.nodesArray);
      _this.edges.add(_this.edgesArray);
      _this.data = {
        nodes: _this.nodes,
        edges: _this.edges
      };
      //   network是一种用于将包含点和线的网络和网络之间的可视化展示
      _this.network = new Vis.Network(
        _this.container,
        _this.data,
        _this.options
      );
    },
    resetAllNodesStabilize() {
      let _this = this;
      _this.resetAllNodes();
      _this.network.stabilize();
    }
  },
 
  mounted() {
    this.init();
    // 点击事件
    this.network.on("click", params => {
      console.log("点击", params.nodes);
      // this.network.addEdgeMode();
    });
    // 点击鼠标右键事件
    this.network.on("oncontext", params => {
      console.log("右击", params);
      this.dialogVisible = true;
    });
  }
};
</script>
  
<style scoped>
.author-name {
  font-size: 20px;
  font-weight: 700;
  line-height: 1.4;
  font-family: Tahoma,fantasy;
}

.abstract {
    font-family: Georgia, Lato-Regular,Lato,sans-serif;
    font-size: 15px;
    line-height: 22px;
    color: #262625;
}
</style>