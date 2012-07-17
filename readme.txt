.. _index:

Django 最佳实践 - 中文版 (2009-06-17)
=========================================

:注意:

    注意：英文指南 (`django-best-practices`_) 很久没有更新，这份译文的内容可能已经过时，仅用来参考，勿用来作为开发准则。

:翻译:
    .. line-block::

        `brantyoung <http://yangyubo.com>`_

:项目主页:
    - `django-best-practices`_
    - `django-best-practices - 中文版 <https://github.com/brantyoung/zh-django-best-practices>`_

.. _readme:

译者 (yospaly) 前言
--------------------

**Django 最佳实践** (`django-best-practices`_) 是 `django-reusable-app-docs`_ 的一个分支项目, 它在原有项目的理念上进行了扩展, 建立了一套关于 Django Web 开发方面的 "最佳实践" 规则, 这些理念超出了官方文档的讨论范围.

这份文档由一系列准则组成, 围绕这如何创建便于维护, 代码干净, 结构清晰, 方便复用, 易于部署的 Django 项目. 对于初学者, 它是一份不可多得指南, 如果不知道从何下手, 按照文档说做能很快规范起来; 对于经验丰富 Django 达人, 它也有一定的参考价值, 可以据此来创建自己的最佳实践准则.

原文是多页面方式, 不过 **实践** 每个规则的内容并不太多, 打散成多页面反而浏览不方便. 所以我把它们全合并到单个页面中, 除此之外, 没做其它改动.

原文和译文的源文件均使用 `reStructuredText <http://docutils.sourceforge.net/>`__ 格式, 可以用 `Sphinx <http://sphinx.pocoo.org>`__ 转换成 HTML 等格式的文档.

+ `中文最新版本在线文档 <https://github.com/brantyoung/zh-django-best-practices/blob/master/readme.rst/>`__

.. note:: 中文版力求保持和英文版同步更新. 当前版本 2009-06-17 11:32:35

.. _best_practices:

Django 最佳实践
=================

这是一份关于开发和部署 `Django Web 框架 <http://www.djangoproject.com>`__ 的动态文档 (会随时更新). 这些准则不应该被认为是 *绝对正确* 或 *唯一* 使用 Django 的方法, 应该说这些最佳实践是我们使用框架多年来积累的经验.

本项目是 `django-reusable-app-docs 项目`_ 的一个分支, 这个优秀的项目是由 `Brian Rosner <http://oebfare.com>`__ 和 `Eric Holscher <http://ericholscher.com>`_ 建立的, 是关于如何开发和维护可复用 Django apps 方面的最佳实践准则.

.. _django-reusable-app-docs 项目: http://github.com/ericholscher/django-reusable-app-docs/

.. note::
    这份文档的源码放在 GitHub `django-best-practices`_ , 可以用 `Sphinx <http://sphinx.pocoo.org>`__ 转换成多种文档格式

.. _django-best-practices: http://github.com/lincolnloop/django-best-practices/


.. _code:
.. index:: Coding Conventions, PEP 8, PEP 20
   pair: Python; Coding Conventions
   pair: Django; Coding Conventions

代码风格
----------

一般而言, 代码应该干净, 简明, 易读. `The Zen of Python (PEP 20) <http://www.python.org/dev/peps/pep-0020/>`_ 是 Python 编码实践的权威介绍.

+ 尽可能合理的遵守 `Style Guide for Python Code (PEP 8)
  <http://www.python.org/dev/peps/pep-0008/>`__.
+ 遵守 `Django coding style
  <http://docs.djangoproject.com/en/dev/internals/contributing/#coding-
  style>`__.


.. _apps:

Django 应用 (app)
-------------------

.. _apps-distribution:

如何发布我的 app ?
~~~~~~~~~~~~~~~~~~~~

Django 应该使用使用标准的 `Python Package Index
<http://pypi.python.org/pypi>`__ 即 Pypi 和 Cheese Shop. 我写过一篇关于如何
轻松打包和上传 app 到 Pypi 的 `教程 <http://ericholscher.com/blog/2008/aug/6/easily-packing-
and-distributing-django-apps-setupt/>`__.

如果你上传 app 到 Pypi, 建议最好在你的项目名前加上 "django-" 前缀.

(yospaly: 以下不解其意, 望达人指点)
Also note, that when below when we refer to the default place for
something as a file, that also means that you can make a directory of
that same name; as per normal python.


.. _apps-documentation:

文档
~~~~~~~~~~~~~~~~~~~~

+ 放在和 APP 目录同级的 docs 目录中 (你的 app 应该有上级目录的吧?)
+ 可以包含模板, 供使用者参考


.. _apps-overview:
   pair: What are; Reusable Apps
   triple: James Bennett; Djangocon Talk; Reusable Apps

什么是可复用 app?
~~~~~~~~~~~~~~~~~~~

一个 Django app, 一个能够轻松嵌入到 project 的 app, 提供一个非常明确的功能.
它们应该专注并遵循 Unix 哲学 -- "做一件事并把它做好". 更多相关信息请参考 James Bennett 的
`Djangocon talk <http://www.youtube.com/watch?v=A-S0tqpPga4>`__.


.. _apps-modules:

Application 模块
~~~~~~~~~~~~~~~~~~~~~~

(yospaly: 以下所有大写单词, 如: APP, MODEL 等, 替换成你项目中真实的 app 名或 model 名.)

.. _apps-admin:

Admin
^^^^^^^^^^^^^

+ 非必须
+ 放在 APP/admin.py 文件中
+ Admin 的 MODEL 类命名为 MODELAdmin

.. _apps-context_processors:

上下文处理器
^^^^^^^^^^^^^^^^^^

+ 放在 APP/context_processors.py 文件中



.. _apps-feeds:

内容源
^^^^^^^^^^^^^^

+ 放在 APP/feeds.py 文件中


.. _apps-forms:

表单
^^^^^^^^^^^^^^

+ 放在 APP/forms.py 文件中


.. _apps-managers:

Managers
^^^^^^^^^

+ 放在 APP/managers.py 文件中


.. _apps-middleware:

中间件
^^^^^^^^^^^^^^^^^^^^

+ 放在 APP/middleware.py 文件中
+ 实现尽可能少的任务


.. _apps-models:

模型
^^^^^^^^^^^^^^

+ 放在 APP/models (.py 文件中或目录下)
+ 遵循 `Django's 模型约定
  <http://docs.djangoproject.com/en/dev/internals/contributing/#model-
  style>`__


.. _apps-templates:

模板
^^^^^^^^^^^^^^^^^

+ 放在 APP/templates/APP/template.html 文件中

为了尽量标准化 Django 模板区块 (block) 名称, 我建议通常情况下使用以下区块名称.

+ {% block title %}

这个区块用来定义页面的标题. 你的 base.html 模板很可能要在这个 tag 之外定义
站点名字 (Site's name) (即便使用了 Sites 框架), 以便能够放在所有页面中.


+ {% block extra_head %}

我认为这是个非常有用的区块, 很多人已经以某种方式在使用了.
很多页面经常需要在 HTML 文档头添加些信息, 比如 RSS 源, Javascript,
CSS, 以及别的应该放在文档头的信息. 你可以, 也很可能将会, 定义另外专门的区块
(比如前面的 title 区块) 来添加文档头的其它部分的信息.


+ {% block body %}

这个 tag 用来包含页面的整个 body 部分. 这使得你在 app 中创建的页面
能够替换整个页面内容, 不仅仅是正文内容. 这种做法虽不常见, 但当你需要时,
它确实是一个非常方便的 tag. 你可能还没注意到, 我一直尽可能的使 tag
名字和 HTML 标签名称保持一致.


+ {% block menu %}

你的菜单 (导航栏) 应该包含在这个区块中. 它是针对站点级的导航, 不是
每个页面专属的导航菜单.


+ {% block content %}

这个区块用来放置页面正文内容. 任何页面正文内容都可能不一样. 它不
包含任何站点导航, 信息头, 页脚, 或其它任何属于 base 模板的东东.


其它可能的区块
++++++++++++++++


+ {% block content_title %}

用来指定 content 区块的 "title". 比如 blog 的标题. 也可以用来
包含 content 内的导航 (译注: 比如提纲), 或其它类似的东东. 大致都是些
页面中并非主要内容的东东. 我不知道这个区块是否应该放到 `content` tag 内,
并且对应于前面建议的 `content` tag, 是不是还需要一个 `main_content` 区块.

+ {% block header %} {% block footer %}

任何每个页面都可能修改的文本区域的页面和页脚.


+ {% block body_id %} {% block body_class %}

用来设置 HTML 文档 body 标签的 class 或 id 属性. 在设置样式或其它属性时
非常有用.


+ {% block [section]_menu %} {% block page_menu %}

这是对应于之前建议的 `menu` 区块. 用来导航一个章节或页面.


.. _apps-templatetags:

模板标签
^^^^^^^^^^^^^^^^^^^^^^^^


+ 放在 APP/templatetags/APP_tags.py 文件中


推荐的模板标签语法
+++++++++++++++++++++++++

+ as (Context Var): This is used to set a variable in the context of
  the page
+ for (object or app.model): This is used to designate an object for
  an action to be taken on.
+ limit (num): This is used to limit a result to a certain number of
  results.
+ exclude (object or pk): The same as for, but is used to exclude
  things of that type.


.. _apps-tests:

测试
^^^^^^^^

+ 放在 APP/tests (.py 文件或目录) 中
+ Fixtures 放在 APP/fixtures/fixture.json 文件中
+ 通常只须重写 Django 的 `testcase
  <http://docs.djangoproject.com/en/dev/topics/testing/#testcase>`__


.. _apps-urls:

URLs
^^^^^^^^^^^^^^^^

+ 放在 APP/urls (.py 文件或目录) 中
+ 需要设置 name 属性以便能够被反查; name 属性设置成 APP_MODEL_VIEW 的格式,
  比如 blog_post_detail 或 blog_post_list.

.. _apps-views:

视图
^^^^^^^^^^^^^^^^

+ 放在 APP/views (.py 文件或目录) 中
+ 可以是任何可调用的 python 函数.
+ 视图参数应提供合理的缺省值, 并易于定制:


范例:

.. sourcecode:: python

        def register(request, success_url=None,
                 form_class=RegistrationForm
                 template_name='registration/registration_form.html',
                 extra_context=None):



.. _projects:

Django Projects (项目)
-----------------------

.. _projects-layout:

推荐的布局
~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: python

     example.com/
        README
        settings.py
        urls.py
        docs/
            This will hold the documentation for your project
        static/
            -In production this will be the root of your MEDIA_URL
            css/
            js/
            images/
        tests/
            - Project level tests (Each app should also have tests)
        uploads/
            - content imgs, etc
        templates/
            - This area is used to override templates from your reusable apps
            flatpages/
            comments/
            example/
            app1/
            app2/




.. _projects-overview:

什么是 Django Project?
~~~~~~~~~~~~~~~~~~~~~~~~~

Django 中的 project 指的是一个包含设置文件, urls 链接, 以及一些 Django Apps
集合的简单结构. 这些东东可以是你自己写的, 也可以是一些包含在你的 project 内
的第三方代码.


.. _projects-modules:

Project 模块
~~~~~~~~~~~~~~~~~~~~~~

.. _projects-settings:

设置
^^^^^^^^^^^

放在 ``[PROJECT]/settings.py`` 文件中

使用相对路径

.. sourcecode:: python

    import os
    DIRNAME = os.path.dirname(__file__)

    MEDIA_ROOT = os.path.join(DIRNAME, 'static')

具体环境相关的设置使用 ``local_settings.py`` 文件, 并在 ``settings.py`` 文件结尾导入它.

.. sourcecode:: python

    try:
        from local_settings import *
    except ImportError:
        pass


.. _projects-urls:

URLs
^^^^^^^^^^^

+ 放在 PROJECT/urls.py 文件中
+ 应包含最少的逻辑代码, 多数情况下只作为一个指针, 指向你 apps 各自的 URL 配置.


.. _deployment:

部署
---------

.. _deployment-bootstrap:

Project 的环境初始化
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: virtualenv, pip

.. _deployment-filesystem_layout:

文件系统布局
^^^^^^^^^^^^^^^^^^^^^

.. note:: 本文档严重偏向 Unix 风格的文件系统, 要在其它操作系统上使用需要做些额外的修改.

`Virtualenv <http://pypi.python.org/pypi/virtualenv>`_ 对于 Python 项目来说是必须的. 它提供一个隔离不同 Python 运行环境的方法.
典型的, 我们在 ``/opt/webapps/<site_name>`` 部署生产环境站点, 在 ``~/webapps/<site_name>`` 目录部署我们的开发环境站点.
每个 project 有它自己的 ``virtualenv``, ``virtualenv`` 还充当 project 所有相关代码的根目录. 我们使用 ``pip`` 为 ``virtualenv``
添加必要的包.

引导过程看上去是这样的:

.. sourcecode:: bash

    cd /opt/webapps
    virtualenv mysite.com
    cd mysite.com
    pip install -E . -r path/to/requirements.txt
    source bin/activate

.. tip:: 方便起见, 你可以在你的 ``virtualenv`` 根目录中创建 Django project 的符号链接. 符号链接的名字无所谓, 因为你的 project 已经在 Python 搜索路径中. 通过给你所有的 projects 起同样的符号链接名, 你可以使用一些 `方便的 bash 函数以节省时间 <http://gist.github.com/91456>`_.

.. index:: pip, requirements.txt


.. _deployment-packaging:

打包
^^^^^^^^^^^^^^^^^^^^^

成功部署的关键之一是, 保证你开发环境下的软件尽可能接近部署环境下的软件. `Pip <http://pip.openplans.org>`_ 提供了一个简单的重现方法, 让你在任何系统上都能非常一致的部署 Python 项目. 任何需要第三方库的 app 都应该包含一个名为 ``requirements.txt`` 的 `pip 规格文件 <http://pip.openplans.org/#requirements-files>`_. Projects 应到负责汇集所有 app 的规格文件, 并在根据需要添加其它规格.

.. rubric:: 你的规格文件中要包含些什么

我们的经验是, 任何应用程序, 只要你的操作系统默认没附带. 唯一需要从我们的规格文件中剔除的几个包是 ``PIL``, 数据库驱动和其它 ``pip`` 不能安装的包. 这些被剔除的规格放在 :ref:`project's README <projects-layout>` 文件中加以说明.


.. _deployment-servers:

服务器
~~~~~~~~~~~~~~~~~~~~~~~

.. note:: 部署架构很大程度上取决于站点的流量. 下面描述的设置对我们来说, 在大多数情况下工作的最好.

我们基于 Linux 和 PostgreSQL 后端数据库部署 Django, `Nginx <http://nginx.net>`__ 进程作为前端代理, 处在其后的是 Apache 和 `mod_wsgi <http://www.modwsgi.org>`__.

.. _deployment-nginx:

.. index:: Nginx

Nginx
^^^^^^^^^^^

`Nginx <http://nginx.net>`__ 是一个非常优秀的前端服务器, 速度快, 稳如磐石, 并且资源占用很少. 以下是一个典型的 Nginx 站点配置:

.. literalinclude:: /examples/nginx.conf
    :language: nginx

.. rubric:: 它都做些什么?

第一段告诉 Nginx 去哪里找托管了 Django 站点的服务器. 第二段把所有来自 ``www.domain.com`` 的请求重定向到 ``domain.com``, 这样所有资源就都只有一个 URL 能被访问到. 最后一段承担了所有工作. 它告诉 Nginx 检查 ``/var/www/domain.com`` 中是否存在被请求的文件. 如果存在, 它返回该文件, 否则, 它将把请求转发给 Django 站点.

.. warning:: yospaly 注

    以下涉及 Apache 的部分均未作翻译, 我们强烈建议使用 Nginx/Lighttpd + SCGI/FastCGI/HTTP 的方式, 尽量不要使用繁琐的 Apache + mod_wsgi.

.. index::
    pair: Nginx; SSL

SSL
^^^

Another benefit to running a frontend server is lightweight SSL proxying. Rather than having two Django instances running for SSL and non-SSL access, we can have Nginx act as the gatekeeper redirecting all requests back to a single non-SSL Apache instance listening on the ``localhost``. Here's what that would look like:

.. literalinclude:: /examples/nginx_ssl.conf
    :language: nginx

You can include this code at the bottom of your non-SSL configuration file.

.. tip:: For SSL-aware Django sites like `Satchmo <http://www.satchmoproject.com>`_, you'll need to "trick" the site into thinking incoming requests are coming in via SSL, but this is simple enough to do with `a small addition to the WSGI script <http://gist.github.com/78416>`_ we discuss below.

.. index:: Apache
    pair: Apache; mod_wsgi
    pair: Apache; Worker MPM
    pair: Apache; Listen

Apache
------

We run the Apache2 Worker MPM with `mod_wsgi <http://www.modwsgi.org>`__ in daemon mode. The default settings for the MPM Worker module should be sufficient for most environments although those with a shortage of RAM may want to look into reducing the number of servers spawned. Since Nginx will be listening for HTTP(S) requests, you'll need to bind Apache to a different port. While you're at it, you can tell it to only respond to the ``localhost``. To do so, you'll want to edit the `Listen directive <http://httpd.apache.org/docs/2.2/mod/mpm_common.html#listen>`_

.. sourcecode:: apache

    Listen 127.0.0.1:9000

.. index:: mod_wsgi

With Apache up and running, you'll need an Apache configuration and WSGI script for each site. A typical Apache configuration for an individual site looks like this:

.. literalinclude:: /examples/apache.conf
    :language: apache

.. index::
    pair: mod_wsgi; maximum-requests

.. tip:: In a perfect world, your app would never leak memory and you can leave out the ``maximum-requests`` directive. In our experience, setting this to a high number is nice to keep Apache's memory usage in check.

.. warning:: This will default to a single process with 15 threads. Django is not "officially" thread safe and some external libraries (notably a couple required for ``django.contrib.gis``) are known to not be thread safe. If needed the ``threads`` and ``processes`` arguments can be adjusted accordingly.

It links to the WSGI script within the project directory. The script is just a few lines of Python to properly setup our environment.

.. literalinclude:: /examples/django.wsgi
    :language: python
