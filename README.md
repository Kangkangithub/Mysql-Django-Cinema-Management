# Django 电影院管理系统

✨ **基于 Django 和 MySQL 的电影院后台管理系统** ✨

一个功能完整的电影院管理系统，包含影片管理、影厅管理、排片管理、座位管理、用户管理、订单管理等核心功能。采用 Django 框架开发，支持 MySQL 数据库，提供完整的后台管理界面。

## 🚀 项目概述

### 主要功能
- **影片管理**：影片信息的增删改查，包括影片名称、类型、时长、导演、演员等
- **影厅管理**：影厅信息管理，座位数量配置
- **排片管理**：电影排片计划，时间安排，票价设置
- **座位管理**：座位状态管理（可用、已预订、已锁定）
- **用户管理**：用户信息管理，账户余额管理
- **订单管理**：票务订单处理，支付状态跟踪
- **管理员系统**：后台管理员权限控制

### 技术特点
- 前后端不分离的传统 Web 应用
- 完整的 CRUD 操作
- 用户认证和权限管理
- 响应式 Web 界面
- 数据库事务处理
- 分页功能
- 表单验证

## 🛠️ 技术栈

### 后端技术
- **Python 3.8+** - 编程语言
- **Django 4.2** - Web 框架
  - Django ORM - 对象关系映射
  - Django Forms - 表单处理
  - Django Templates - 模板引擎
  - Django Middleware - 中间件
  - Django Admin - 后台管理
- **MySQL 8.0+** - 关系型数据库
- **mysqlclient 2.1.1** - MySQL 数据库连接器

### 前端技术
- **HTML5** - 页面结构
- **CSS3** - 样式设计
- **JavaScript** - 交互逻辑
- **jQuery 3.6.4** - JavaScript 库
- **Bootstrap 5.3.0** - CSS 框架
  - 响应式布局
  - 组件库
  - 图标库
- **Bootstrap Icons 1.10.4** - 图标库
- **FontAwesome 6.4.0** - 图标字体

### 开发工具
- **Git** - 版本控制
- **PyCharm/VSCode** - 开发环境
- **MySQL Workbench** - 数据库管理工具

### 架构模式
- **MVC 架构** - Model-View-Controller
- **Django MVT** - Model-View-Template
- **RESTful 设计** - 资源导向的 URL 设计

## 📋 环境要求

### 系统要求
- Python 3.8 或更高版本
- MySQL 8.0 或更高版本
- pip 包管理器

### 依赖包
```
django==4.2
mysqlclient==2.1.1
```

## 🔧 安装指南

### 1. 克隆项目
```bash
git clone <repository-url>
cd Mysql-Django-Cinema-Management
```

### 2. 创建虚拟环境（推荐）
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. 安装依赖
```bash
pip install -r requirement.txt
```

### 4. 数据库配置

#### MySQL 配置
1. 确保 MySQL 服务正在运行
2. 创建数据库：
```sql
CREATE DATABASE djangolearntest CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

3. 修改 `Learntest/settings.py` 中的数据库配置：
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangolearntest',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

#### SQLite 配置（可选）
如果使用 SQLite，取消注释以下配置：
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

### 5. 数据库迁移
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. 创建管理员账户
```bash
python manage.py shell
```

在 Django shell 中执行：
```python
import app01.models
app01.models.MyAdmin.objects.create(id="admin", user_name="admin", password="9b7bdac3cbd4af86551d5f27d64a5291")
exit()
```

### 7. 启动服务器
```bash
python manage.py runserver
```

或指定端口：
```bash
python manage.py runserver 8008
```

### 8. 访问系统
- 访问地址：http://127.0.0.1:8000
- 管理员账号：`admin`
- 管理员密码：`12345678`

## 📁 项目结构

```
Mysql-Django-Cinema-Management/
├── manage.py                    # Django 管理脚本
├── requirement.txt              # 项目依赖
├── README.md                   # 项目说明
├── LICENSE                     # 开源协议
├── .gitignore                  # Git 忽略文件
├── Learntest/                  # Django 项目配置
│   ├── __init__.py
│   ├── settings.py             # 项目设置
│   ├── urls.py                 # 主路由配置
│   ├── wsgi.py                 # WSGI 配置
│   └── asgi.py                 # ASGI 配置
├── app01/                      # 主应用
│   ├── __init__.py
│   ├── admin.py                # Django Admin 配置
│   ├── apps.py                 # 应用配置
│   ├── models.py               # 数据模型
│   ├── views.py                # 视图函数
│   ├── tests.py                # 测试文件
│   ├── migrations/             # 数据库迁移文件
│   ├── middle_ware/            # 自定义中间件
│   │   └── my_auth.py          # 认证中间件
│   ├── srcs/                   # 源码目录
│   │   ├── forms/              # 表单定义
│   │   │   └── form.py
│   │   └── views/              # 视图模块
│   │       ├── account.py      # 账户管理
│   │       ├── movies.py       # 影片管理
│   │       ├── halls.py        # 影厅管理
│   │       ├── schedules.py    # 排片管理
│   │       ├── seats.py        # 座位管理
│   │       ├── user.py         # 用户管理
│   │       ├── order.py        # 订单管理
│   │       └── myadmin.py      # 管理员管理
│   ├── static/                 # 静态文件
│   │   ├── jquery-3.6.4.min.js
│   │   ├── bootstrap-5.3.0-alpha1-dist/
│   │   ├── bootstrap-icons-1.10.4/
│   │   └── fontawesome-free-6.4.0-web/
│   ├── templates/              # 模板文件
│   │   ├── layout.html         # 基础模板
│   │   ├── index.html          # 首页
│   │   ├── account/            # 账户相关模板
│   │   ├── movie/              # 影片管理模板
│   │   ├── hall/               # 影厅管理模板
│   │   ├── schedules/          # 排片管理模板
│   │   ├── seat/               # 座位管理模板
│   │   ├── users/              # 用户管理模板
│   │   ├── order/              # 订单管理模板
│   │   └── myadmin/            # 管理员模板
│   └── utils/                  # 工具模块
│       ├── bootstrap_modelform.py  # Bootstrap 表单
│       ├── md5.py              # MD5 加密
│       └── page_nav.py         # 分页导航
└── readme_img/                 # 说明文档图片
```

## 🎯 功能模块

### 1. 用户管理系统
- **用户信息管理**：姓名、年龄、性别、邮箱、账户余额
- **用户认证**：登录验证、权限控制
- **账户管理**：余额查询、充值记录
- **分页显示**：支持大量用户数据的分页浏览
- **搜索功能**：按用户名搜索

### 2. 影片管理
- **影片信息**：标题、类型、时长、导演、演员阵容、上映日期
- **CRUD 操作**：创建、读取、更新、删除影片信息
- **影片列表**：展示所有影片信息
- **影片编辑**：修改影片详细信息

### 3. 影厅管理
- **影厅信息**：影厅名称、座位总数
- **影厅分配**：为影厅分配正在播放的影片
- **容量管理**：座位数量配置
- **状态管理**：影厅使用状态

### 4. 排片管理
- **排片计划**：影片、影厅、放映时间的组合
- **票价设置**：不同场次的票价配置
- **时间管理**：放映时间安排
- **场次查询**：按影片或时间查询场次

### 5. 座位管理
- **座位状态**：可用、已预订、已锁定
- **座位编号**：行列座位号管理（如 A1、B5）
- **实时更新**：座位状态实时同步
- **批量操作**：批量座位状态管理

### 6. 订单管理
- **订单创建**：用户购票订单生成
- **支付状态**：待支付、支付中、已支付
- **订单查询**：按用户、时间、状态查询
- **订单详情**：完整的购票信息

### 7. 管理员系统
- **权限控制**：管理员登录验证
- **密码管理**：密码重置功能
- **操作日志**：管理员操作记录
- **系统配置**：基础系统参数设置

## 🔗 数据库设计

### 核心数据表
- **Movie（影片表）**：存储影片基本信息
- **Hall（影厅表）**：影厅信息和座位配置
- **UserInfo（用户表）**：用户账户信息
- **Schedule（排片表）**：排片计划和票价
- **Seat（座位表）**：座位状态管理
- **Order（订单表）**：购票订单信息
- **MyAdmin（管理员表）**：系统管理员信息

### 关系设计
- 影片与排片：一对多关系
- 影厅与排片：一对多关系
- 排片与座位：一对多关系
- 用户与订单：一对多关系
- 座位与订单：一对一关系

## 🎨 界面展示

系统采用 Bootstrap 5 响应式设计，界面简洁美观：

- **登录界面**：简洁的管理员登录页面
- **主控制台**：功能模块导航
- **数据列表**：表格形式展示数据，支持分页
- **表单页面**：用户友好的数据录入界面
- **响应式设计**：适配不同屏幕尺寸

## 🚀 使用说明

### 管理员操作流程
1. **登录系统**：使用管理员账号登录
2. **影片管理**：添加新影片，编辑影片信息
3. **影厅配置**：设置影厅信息和座位数
4. **排片安排**：为影片安排放映时间和影厅
5. **座位管理**：监控座位预订状态
6. **用户管理**：管理用户账户信息
7. **订单处理**：查看和处理购票订单

### 系统维护
- **数据备份**：定期备份 MySQL 数据库
- **日志监控**：查看 Django 运行日志
- **性能优化**：监控数据库查询性能
- **安全更新**：及时更新依赖包版本

## 🔧 开发指南

### 代码结构
- **models.py**：定义数据模型和数据库关系
- **views.py**：处理 HTTP 请求和响应
- **forms.py**：定义表单验证规则
- **templates/**：HTML 模板文件
- **static/**：静态资源文件
- **utils/**：通用工具函数

### 自定义功能
- **中间件**：`my_auth.py` 实现用户认证
- **分页组件**：`page_nav.py` 提供分页功能
- **表单组件**：`bootstrap_modelform.py` 集成 Bootstrap 样式
- **加密工具**：`md5.py` 提供密码加密

### 扩展建议
- 添加 RESTful API 接口
- 集成支付系统
- 添加短信/邮件通知
- 实现数据统计和报表
- 添加移动端支持

## 🤝 贡献指南

欢迎贡献代码！请遵循以下步骤：

### 贡献流程
1. **Fork 项目**到你的 GitHub 账户
2. **创建功能分支**：`git checkout -b feature/AmazingFeature`
3. **提交更改**：`git commit -m 'Add some AmazingFeature'`
4. **推送分支**：`git push origin feature/AmazingFeature`
5. **创建 Pull Request**

### 代码规范
- 遵循 PEP 8 Python 代码规范
- 添加适当的注释和文档字符串
- 编写单元测试
- 确保代码通过所有测试

### 问题报告
- 使用 GitHub Issues 报告 bug
- 提供详细的错误信息和复现步骤
- 建议新功能时请详细描述需求

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 📞 联系方式

如有问题或建议，请通过以下方式联系：

- 创建 GitHub Issue
- 发送邮件至项目维护者
- 参与项目讨论

## 🙏 致谢

感谢所有为这个项目做出贡献的开发者和用户！

---

**⭐ 如果这个项目对你有帮助，请给它一个 Star！**
