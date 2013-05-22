  


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>siga-tools-doc-reqbox-txt/reqbox/tests/rbmodel8_tests.py at newtemplate · vonpupp/siga-tools-doc-reqbox-txt · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="http://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <link rel="xhr-socket" href="/_sockets" />


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" />

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="Slx3at77MRlWe0ycdNL9wm2FiJ8OtqCRg/JWcQgGzlI=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/assets/github-159290696eb4150b6abdc4ac7fa8da500bcca10f.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/assets/github2-0d894c14747f62f9900dc75a936d6f8979d8eb92.css" media="all" rel="stylesheet" type="text/css" />
    


      <script src="https://a248.e.akamai.net/assets.github.com/assets/frameworks-92d138f450f2960501e28397a2f63b0f100590f0.js" type="text/javascript"></script>
      <script src="https://a248.e.akamai.net/assets.github.com/assets/github-76cc892ab78e865420ada4b851fbb109aa83cbfc.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="d35cab367dbc001c05b2c7abe21106cb">

        <link data-pjax-transient rel='permalink' href='/vonpupp/siga-tools-doc-reqbox-txt/blob/0cc6bf1d1b43f69bea07fbbcfc0a17c0eee4cfed/reqbox/tests/rbmodel8_tests.py'>
    <meta property="og:title" content="siga-tools-doc-reqbox-txt"/>
    <meta property="og:type" content="githubog:gitrepository"/>
    <meta property="og:url" content="https://github.com/vonpupp/siga-tools-doc-reqbox-txt"/>
    <meta property="og:image" content="https://secure.gravatar.com/avatar/51e431a00f176ac3c3868910508920ef?s=420&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png"/>
    <meta property="og:site_name" content="GitHub"/>
    <meta property="og:description" content="siga-tools-doc-reqbox-txt - SIGA / Tools / It&#39;s a requirements magic file parser (yes in order to deal with MS Office encoding, you need to do magic tricks) that generates multiple files to be used with other tools. Name and py-losophy comes from busybox."/>
    <meta property="twitter:card" content="summary"/>
    <meta property="twitter:site" content="@GitHub">
    <meta property="twitter:title" content="vonpupp/siga-tools-doc-reqbox-txt"/>

    <meta name="description" content="siga-tools-doc-reqbox-txt - SIGA / Tools / It&#39;s a requirements magic file parser (yes in order to deal with MS Office encoding, you need to do magic tricks) that generates multiple files to be used with other tools. Name and py-losophy comes from busybox." />


    <meta content="1082073" name="octolytics-dimension-user_id" /><meta content="4932286" name="octolytics-dimension-repository_id" />
  <link href="https://github.com/vonpupp/siga-tools-doc-reqbox-txt/commits/newtemplate.atom" rel="alternate" title="Recent Commits to siga-tools-doc-reqbox-txt:newtemplate" type="application/atom+xml" />

  </head>


  <body class="logged_out page-blob  vis-public env-production  ">
    <div id="wrapper">

      

      
      
      

      
      <div class="header header-logged-out">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/">Github</a>

    <div class="header-actions">
      <a class="button primary" href="https://github.com/signup">Sign up</a>
      <a class="button" href="https://github.com/login?return_to=%2Fvonpupp%2Fsiga-tools-doc-reqbox-txt%2Fblob%2Fnewtemplate%2Freqbox%2Ftests%2Frbmodel8_tests.py">Sign in</a>
    </div>

    <div class="command-bar js-command-bar  in-repository">


      <ul class="top-nav">
          <li class="explore"><a href="https://github.com/explore">Explore</a></li>
        <li class="features"><a href="https://github.com/features">Features</a></li>
          <li class="blog"><a href="https://github.com/blog">Blog</a></li>
      </ul>
        <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">
  <a href="/search/advanced" class="advanced-search-icon tooltipped downwards command-bar-search" id="advanced_search" title="Advanced search"><span class="octicon octicon-gear "></span></a>

  <input type="text" data-hotkey="/ s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
      data-repo="vonpupp/siga-tools-doc-reqbox-txt"
      data-branch="newtemplate"
      data-sha="b5fe2ad93954c5cf535f8f0645597e7edd8ee33c"
  >

    <input type="hidden" name="nwo" value="vonpupp/siga-tools-doc-reqbox-txt" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="octicon help tooltipped downwards" title="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

  <div class="divider-vertical"></div>

</form>
    </div>

  </div>
</div>


      

      


            <div class="site hfeed" itemscope itemtype="http://schema.org/WebPage">
      <div class="hentry">
        
        <div class="pagehead repohead instapaper_ignore readability-menu ">
          <div class="container">
            <div class="title-actions-bar">
              

<ul class="pagehead-actions">



    <li>
      <a href="/login?return_to=%2Fvonpupp%2Fsiga-tools-doc-reqbox-txt"
        class="minibutton js-toggler-target star-button entice tooltipped upwards"
        title="You must be signed in to use this feature" rel="nofollow">
        <span class="octicon octicon-star"></span>Star
      </a>
      <a class="social-count js-social-count" href="/vonpupp/siga-tools-doc-reqbox-txt/stargazers">
        0
      </a>
    </li>
    <li>
      <a href="/login?return_to=%2Fvonpupp%2Fsiga-tools-doc-reqbox-txt"
        class="minibutton js-toggler-target fork-button entice tooltipped upwards"
        title="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-git-branch"></span>Fork
      </a>
      <a href="/vonpupp/siga-tools-doc-reqbox-txt/network" class="social-count">
        0
      </a>
    </li>
</ul>

              <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
                <span class="repo-label"><span>public</span></span>
                <span class="mega-octicon octicon-repo"></span>
                <span class="author vcard">
                  <a href="/vonpupp" class="url fn" itemprop="url" rel="author">
                  <span itemprop="title">vonpupp</span>
                  </a></span> /
                <strong><a href="/vonpupp/siga-tools-doc-reqbox-txt" class="js-current-repository">siga-tools-doc-reqbox-txt</a></strong>
              </h1>
            </div>

            
  <ul class="tabs">
    <li class="pulse-nav"><a href="/vonpupp/siga-tools-doc-reqbox-txt/pulse" class="js-selected-navigation-item " data-selected-links="pulse /vonpupp/siga-tools-doc-reqbox-txt/pulse" rel="nofollow"><span class="octicon octicon-pulse"></span></a></li>
    <li><a href="/vonpupp/siga-tools-doc-reqbox-txt/tree/newtemplate" class="js-selected-navigation-item selected" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /vonpupp/siga-tools-doc-reqbox-txt/tree/newtemplate">Code</a></li>
    <li><a href="/vonpupp/siga-tools-doc-reqbox-txt/network" class="js-selected-navigation-item " data-selected-links="repo_network /vonpupp/siga-tools-doc-reqbox-txt/network">Network</a></li>
    <li><a href="/vonpupp/siga-tools-doc-reqbox-txt/pulls" class="js-selected-navigation-item " data-selected-links="repo_pulls /vonpupp/siga-tools-doc-reqbox-txt/pulls">Pull Requests <span class='counter'>0</span></a></li>

      <li><a href="/vonpupp/siga-tools-doc-reqbox-txt/issues" class="js-selected-navigation-item " data-selected-links="repo_issues /vonpupp/siga-tools-doc-reqbox-txt/issues">Issues <span class='counter'>0</span></a></li>

      <li><a href="/vonpupp/siga-tools-doc-reqbox-txt/wiki" class="js-selected-navigation-item " data-selected-links="repo_wiki /vonpupp/siga-tools-doc-reqbox-txt/wiki">Wiki</a></li>


    <li><a href="/vonpupp/siga-tools-doc-reqbox-txt/graphs" class="js-selected-navigation-item " data-selected-links="repo_graphs repo_contributors /vonpupp/siga-tools-doc-reqbox-txt/graphs">Graphs</a></li>


  </ul>
  
<div class="tabnav">

  <span class="tabnav-right">
    <ul class="tabnav-tabs">
          <li><a href="/vonpupp/siga-tools-doc-reqbox-txt/tags" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_tags /vonpupp/siga-tools-doc-reqbox-txt/tags">Tags <span class="counter blank">0</span></a></li>
    </ul>
  </span>

  <div class="tabnav-widget scope">


    <div class="select-menu js-menu-container js-select-menu js-branch-menu">
      <a class="minibutton select-menu-button js-menu-target" data-hotkey="w" data-ref="newtemplate">
        <span class="octicon octicon-branch"></span>
        <i>branch:</i>
        <span class="js-select-button">newtemplate</span>
      </a>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">

        <div class="select-menu-modal">
          <div class="select-menu-header">
            <span class="select-menu-title">Switch branches/tags</span>
            <span class="octicon octicon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-filters">
            <div class="select-menu-text-filter">
              <input type="text" id="commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
            </div>
            <div class="select-menu-tabs">
              <ul>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
                </li>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
                </li>
              </ul>
            </div><!-- /.select-menu-tabs -->
          </div><!-- /.select-menu-filters -->

          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="branches">

            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/vonpupp/siga-tools-doc-reqbox-txt/blob/master/reqbox/tests/rbmodel8_tests.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" rel="nofollow" title="master">master</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/vonpupp/siga-tools-doc-reqbox-txt/blob/msbodybegin-fix/reqbox/tests/rbmodel8_tests.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="msbodybegin-fix" rel="nofollow" title="msbodybegin-fix">msbodybegin-fix</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item selected">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/vonpupp/siga-tools-doc-reqbox-txt/blob/newtemplate/reqbox/tests/rbmodel8_tests.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="newtemplate" rel="nofollow" title="newtemplate">newtemplate</a>
                </div> <!-- /.select-menu-item -->
                <div class="select-menu-item js-navigation-item ">
                  <span class="select-menu-item-icon octicon octicon-check"></span>
                  <a href="/vonpupp/siga-tools-doc-reqbox-txt/blob/strucdef/reqbox/tests/rbmodel8_tests.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="strucdef" rel="nofollow" title="strucdef">strucdef</a>
                </div> <!-- /.select-menu-item -->
            </div>

              <div class="select-menu-no-results">Nothing to show</div>
          </div> <!-- /.select-menu-list -->


          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="tags">
            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

            </div>

            <div class="select-menu-no-results">Nothing to show</div>

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

  </div> <!-- /.scope -->

  <ul class="tabnav-tabs">
    <li><a href="/vonpupp/siga-tools-doc-reqbox-txt/tree/newtemplate" class="selected js-selected-navigation-item tabnav-tab" data-selected-links="repo_source /vonpupp/siga-tools-doc-reqbox-txt/tree/newtemplate">Files</a></li>
    <li><a href="/vonpupp/siga-tools-doc-reqbox-txt/commits/newtemplate" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_commits /vonpupp/siga-tools-doc-reqbox-txt/commits/newtemplate">Commits</a></li>
    <li><a href="/vonpupp/siga-tools-doc-reqbox-txt/branches" class="js-selected-navigation-item tabnav-tab" data-selected-links="repo_branches /vonpupp/siga-tools-doc-reqbox-txt/branches" rel="nofollow">Branches <span class="counter ">4</span></a></li>
  </ul>

</div>

  
  
  


            
          </div>
        </div><!-- /.repohead -->

        <div id="js-repo-pjax-container" class="container context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:02fb87db76d9e162cac90c2e393d382c -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:02fb87db76d9e162cac90c2e393d382c -->


<div id="slider">
    <div class="frame-meta">

      <p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

        <div class="breadcrumb">
          <span class='bold'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/vonpupp/siga-tools-doc-reqbox-txt/tree/newtemplate" class="js-slide-to" data-branch="newtemplate" data-direction="back" itemscope="url"><span itemprop="title">siga-tools-doc-reqbox-txt</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/vonpupp/siga-tools-doc-reqbox-txt/tree/newtemplate/reqbox" class="js-slide-to" data-branch="newtemplate" data-direction="back" itemscope="url"><span itemprop="title">reqbox</span></a></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/vonpupp/siga-tools-doc-reqbox-txt/tree/newtemplate/reqbox/tests" class="js-slide-to" data-branch="newtemplate" data-direction="back" itemscope="url"><span itemprop="title">tests</span></a></span><span class="separator"> / </span><strong class="final-path">rbmodel8_tests.py</strong> <span class="js-zeroclipboard zeroclipboard-button" data-clipboard-text="reqbox/tests/rbmodel8_tests.py" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
        </div>

      <a href="/vonpupp/siga-tools-doc-reqbox-txt/find/newtemplate" class="js-slide-to" data-hotkey="t" style="display:none">Show File Finder</a>


        
  <div class="commit file-history-tease">
    <img class="main-avatar" height="24" src="https://secure.gravatar.com/avatar/51e431a00f176ac3c3868910508920ef?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
    <span class="author"><a href="/vonpupp" rel="author">vonpupp</a></span>
    <time class="js-relative-date" datetime="2012-11-28T10:45:05-08:00" title="2012-11-28 10:45:05">November 28, 2012</time>
    <div class="commit-title">
        <a href="/vonpupp/siga-tools-doc-reqbox-txt/commit/f5411d1707b4e568b44178bd3993b2b791323ebf" class="message">minor refactoring and os detection for windows EA api tests integration</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>1</strong> contributor</a></p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2>Users on GitHub who have contributed to this file</h2>
      <ul class="facebox-user-list">
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/51e431a00f176ac3c3868910508920ef?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/vonpupp">vonpupp</a>
        </li>
      </ul>
    </div>
  </div>


    </div><!-- ./.frame-meta -->

    <div class="frames">
      <div class="frame" data-permalink-url="/vonpupp/siga-tools-doc-reqbox-txt/blob/0cc6bf1d1b43f69bea07fbbcfc0a17c0eee4cfed/reqbox/tests/rbmodel8_tests.py" data-title="siga-tools-doc-reqbox-txt/reqbox/tests/rbmodel8_tests.py at newtemplate · vonpupp/siga-tools-doc-reqbox-txt · GitHub" data-type="blob">

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="octicon octicon-file-text"></b></span>
                <span class="mode" title="File Mode">file</span>
                  <span>488 lines (420 sloc)</span>
                <span>16.688 kb</span>
              </div>
              <div class="actions">
                <div class="button-group">
                      <a class="minibutton js-entice" href=""
                         data-entice="You must be signed in and on a branch to make or propose changes">Edit</a>
                  <a href="/vonpupp/siga-tools-doc-reqbox-txt/raw/newtemplate/reqbox/tests/rbmodel8_tests.py" class="button minibutton " id="raw-url">Raw</a>
                    <a href="/vonpupp/siga-tools-doc-reqbox-txt/blame/newtemplate/reqbox/tests/rbmodel8_tests.py" class="button minibutton ">Blame</a>
                  <a href="/vonpupp/siga-tools-doc-reqbox-txt/commits/newtemplate/reqbox/tests/rbmodel8_tests.py" class="button minibutton " rel="nofollow">History</a>
                </div><!-- /.button-group -->
              </div><!-- /.actions -->

            </div>
                <div class="blob-wrapper data type-python js-blob-data">
      <table class="file-code file-diff">
        <tr class="file-code-line">
          <td class="blob-line-nums">
            <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>
<span id="L273" rel="#L273">273</span>
<span id="L274" rel="#L274">274</span>
<span id="L275" rel="#L275">275</span>
<span id="L276" rel="#L276">276</span>
<span id="L277" rel="#L277">277</span>
<span id="L278" rel="#L278">278</span>
<span id="L279" rel="#L279">279</span>
<span id="L280" rel="#L280">280</span>
<span id="L281" rel="#L281">281</span>
<span id="L282" rel="#L282">282</span>
<span id="L283" rel="#L283">283</span>
<span id="L284" rel="#L284">284</span>
<span id="L285" rel="#L285">285</span>
<span id="L286" rel="#L286">286</span>
<span id="L287" rel="#L287">287</span>
<span id="L288" rel="#L288">288</span>
<span id="L289" rel="#L289">289</span>
<span id="L290" rel="#L290">290</span>
<span id="L291" rel="#L291">291</span>
<span id="L292" rel="#L292">292</span>
<span id="L293" rel="#L293">293</span>
<span id="L294" rel="#L294">294</span>
<span id="L295" rel="#L295">295</span>
<span id="L296" rel="#L296">296</span>
<span id="L297" rel="#L297">297</span>
<span id="L298" rel="#L298">298</span>
<span id="L299" rel="#L299">299</span>
<span id="L300" rel="#L300">300</span>
<span id="L301" rel="#L301">301</span>
<span id="L302" rel="#L302">302</span>
<span id="L303" rel="#L303">303</span>
<span id="L304" rel="#L304">304</span>
<span id="L305" rel="#L305">305</span>
<span id="L306" rel="#L306">306</span>
<span id="L307" rel="#L307">307</span>
<span id="L308" rel="#L308">308</span>
<span id="L309" rel="#L309">309</span>
<span id="L310" rel="#L310">310</span>
<span id="L311" rel="#L311">311</span>
<span id="L312" rel="#L312">312</span>
<span id="L313" rel="#L313">313</span>
<span id="L314" rel="#L314">314</span>
<span id="L315" rel="#L315">315</span>
<span id="L316" rel="#L316">316</span>
<span id="L317" rel="#L317">317</span>
<span id="L318" rel="#L318">318</span>
<span id="L319" rel="#L319">319</span>
<span id="L320" rel="#L320">320</span>
<span id="L321" rel="#L321">321</span>
<span id="L322" rel="#L322">322</span>
<span id="L323" rel="#L323">323</span>
<span id="L324" rel="#L324">324</span>
<span id="L325" rel="#L325">325</span>
<span id="L326" rel="#L326">326</span>
<span id="L327" rel="#L327">327</span>
<span id="L328" rel="#L328">328</span>
<span id="L329" rel="#L329">329</span>
<span id="L330" rel="#L330">330</span>
<span id="L331" rel="#L331">331</span>
<span id="L332" rel="#L332">332</span>
<span id="L333" rel="#L333">333</span>
<span id="L334" rel="#L334">334</span>
<span id="L335" rel="#L335">335</span>
<span id="L336" rel="#L336">336</span>
<span id="L337" rel="#L337">337</span>
<span id="L338" rel="#L338">338</span>
<span id="L339" rel="#L339">339</span>
<span id="L340" rel="#L340">340</span>
<span id="L341" rel="#L341">341</span>
<span id="L342" rel="#L342">342</span>
<span id="L343" rel="#L343">343</span>
<span id="L344" rel="#L344">344</span>
<span id="L345" rel="#L345">345</span>
<span id="L346" rel="#L346">346</span>
<span id="L347" rel="#L347">347</span>
<span id="L348" rel="#L348">348</span>
<span id="L349" rel="#L349">349</span>
<span id="L350" rel="#L350">350</span>
<span id="L351" rel="#L351">351</span>
<span id="L352" rel="#L352">352</span>
<span id="L353" rel="#L353">353</span>
<span id="L354" rel="#L354">354</span>
<span id="L355" rel="#L355">355</span>
<span id="L356" rel="#L356">356</span>
<span id="L357" rel="#L357">357</span>
<span id="L358" rel="#L358">358</span>
<span id="L359" rel="#L359">359</span>
<span id="L360" rel="#L360">360</span>
<span id="L361" rel="#L361">361</span>
<span id="L362" rel="#L362">362</span>
<span id="L363" rel="#L363">363</span>
<span id="L364" rel="#L364">364</span>
<span id="L365" rel="#L365">365</span>
<span id="L366" rel="#L366">366</span>
<span id="L367" rel="#L367">367</span>
<span id="L368" rel="#L368">368</span>
<span id="L369" rel="#L369">369</span>
<span id="L370" rel="#L370">370</span>
<span id="L371" rel="#L371">371</span>
<span id="L372" rel="#L372">372</span>
<span id="L373" rel="#L373">373</span>
<span id="L374" rel="#L374">374</span>
<span id="L375" rel="#L375">375</span>
<span id="L376" rel="#L376">376</span>
<span id="L377" rel="#L377">377</span>
<span id="L378" rel="#L378">378</span>
<span id="L379" rel="#L379">379</span>
<span id="L380" rel="#L380">380</span>
<span id="L381" rel="#L381">381</span>
<span id="L382" rel="#L382">382</span>
<span id="L383" rel="#L383">383</span>
<span id="L384" rel="#L384">384</span>
<span id="L385" rel="#L385">385</span>
<span id="L386" rel="#L386">386</span>
<span id="L387" rel="#L387">387</span>
<span id="L388" rel="#L388">388</span>
<span id="L389" rel="#L389">389</span>
<span id="L390" rel="#L390">390</span>
<span id="L391" rel="#L391">391</span>
<span id="L392" rel="#L392">392</span>
<span id="L393" rel="#L393">393</span>
<span id="L394" rel="#L394">394</span>
<span id="L395" rel="#L395">395</span>
<span id="L396" rel="#L396">396</span>
<span id="L397" rel="#L397">397</span>
<span id="L398" rel="#L398">398</span>
<span id="L399" rel="#L399">399</span>
<span id="L400" rel="#L400">400</span>
<span id="L401" rel="#L401">401</span>
<span id="L402" rel="#L402">402</span>
<span id="L403" rel="#L403">403</span>
<span id="L404" rel="#L404">404</span>
<span id="L405" rel="#L405">405</span>
<span id="L406" rel="#L406">406</span>
<span id="L407" rel="#L407">407</span>
<span id="L408" rel="#L408">408</span>
<span id="L409" rel="#L409">409</span>
<span id="L410" rel="#L410">410</span>
<span id="L411" rel="#L411">411</span>
<span id="L412" rel="#L412">412</span>
<span id="L413" rel="#L413">413</span>
<span id="L414" rel="#L414">414</span>
<span id="L415" rel="#L415">415</span>
<span id="L416" rel="#L416">416</span>
<span id="L417" rel="#L417">417</span>
<span id="L418" rel="#L418">418</span>
<span id="L419" rel="#L419">419</span>
<span id="L420" rel="#L420">420</span>
<span id="L421" rel="#L421">421</span>
<span id="L422" rel="#L422">422</span>
<span id="L423" rel="#L423">423</span>
<span id="L424" rel="#L424">424</span>
<span id="L425" rel="#L425">425</span>
<span id="L426" rel="#L426">426</span>
<span id="L427" rel="#L427">427</span>
<span id="L428" rel="#L428">428</span>
<span id="L429" rel="#L429">429</span>
<span id="L430" rel="#L430">430</span>
<span id="L431" rel="#L431">431</span>
<span id="L432" rel="#L432">432</span>
<span id="L433" rel="#L433">433</span>
<span id="L434" rel="#L434">434</span>
<span id="L435" rel="#L435">435</span>
<span id="L436" rel="#L436">436</span>
<span id="L437" rel="#L437">437</span>
<span id="L438" rel="#L438">438</span>
<span id="L439" rel="#L439">439</span>
<span id="L440" rel="#L440">440</span>
<span id="L441" rel="#L441">441</span>
<span id="L442" rel="#L442">442</span>
<span id="L443" rel="#L443">443</span>
<span id="L444" rel="#L444">444</span>
<span id="L445" rel="#L445">445</span>
<span id="L446" rel="#L446">446</span>
<span id="L447" rel="#L447">447</span>
<span id="L448" rel="#L448">448</span>
<span id="L449" rel="#L449">449</span>
<span id="L450" rel="#L450">450</span>
<span id="L451" rel="#L451">451</span>
<span id="L452" rel="#L452">452</span>
<span id="L453" rel="#L453">453</span>
<span id="L454" rel="#L454">454</span>
<span id="L455" rel="#L455">455</span>
<span id="L456" rel="#L456">456</span>
<span id="L457" rel="#L457">457</span>
<span id="L458" rel="#L458">458</span>
<span id="L459" rel="#L459">459</span>
<span id="L460" rel="#L460">460</span>
<span id="L461" rel="#L461">461</span>
<span id="L462" rel="#L462">462</span>
<span id="L463" rel="#L463">463</span>
<span id="L464" rel="#L464">464</span>
<span id="L465" rel="#L465">465</span>
<span id="L466" rel="#L466">466</span>
<span id="L467" rel="#L467">467</span>
<span id="L468" rel="#L468">468</span>
<span id="L469" rel="#L469">469</span>
<span id="L470" rel="#L470">470</span>
<span id="L471" rel="#L471">471</span>
<span id="L472" rel="#L472">472</span>
<span id="L473" rel="#L473">473</span>
<span id="L474" rel="#L474">474</span>
<span id="L475" rel="#L475">475</span>
<span id="L476" rel="#L476">476</span>
<span id="L477" rel="#L477">477</span>
<span id="L478" rel="#L478">478</span>
<span id="L479" rel="#L479">479</span>
<span id="L480" rel="#L480">480</span>
<span id="L481" rel="#L481">481</span>
<span id="L482" rel="#L482">482</span>
<span id="L483" rel="#L483">483</span>
<span id="L484" rel="#L484">484</span>
<span id="L485" rel="#L485">485</span>
<span id="L486" rel="#L486">486</span>
<span id="L487" rel="#L487">487</span>
<span id="L488" rel="#L488">488</span>

          </td>
          <td class="blob-line-code">
                  <div class="highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/env python</span></div><div class='line' id='LC2'><span class="c"># -*- coding: utf-8 -*-</span></div><div class='line' id='LC3'><span class="c">#</span></div><div class='line' id='LC4'><span class="c">#   Project:			SIGA</span></div><div class='line' id='LC5'><span class="c">#   Component Name:		reqbox</span></div><div class='line' id='LC6'><span class="c">#   Language:			Python2</span></div><div class='line' id='LC7'><span class="c">#</span></div><div class='line' id='LC8'><span class="c">#   License: 			GNU Public License</span></div><div class='line' id='LC9'><span class="c">#       This file is part of the project.</span></div><div class='line' id='LC10'><span class="c">#	This is free software: you can redistribute it and/or modify</span></div><div class='line' id='LC11'><span class="c">#	it under the terms of the GNU General Public License as published by</span></div><div class='line' id='LC12'><span class="c">#	the Free Software Foundation, either version 3 of the License, or</span></div><div class='line' id='LC13'><span class="c">#	(at your option) any later version.</span></div><div class='line' id='LC14'><span class="c">#</span></div><div class='line' id='LC15'><span class="c">#	Distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;</span></div><div class='line' id='LC16'><span class="c">#       without even the implied warranty of MERCHANTABILITY or</span></div><div class='line' id='LC17'><span class="c">#       FITNESS FOR A PARTICULAR PURPOSE.</span></div><div class='line' id='LC18'><span class="c">#       See the GNU General Public License for more details.</span></div><div class='line' id='LC19'><span class="c">#       &lt;http://www.gnu.org/licenses/&gt;</span></div><div class='line' id='LC20'><span class="c">#</span></div><div class='line' id='LC21'><span class="c">#   Author:			Albert De La Fuente (www.albertdelafuente.com)</span></div><div class='line' id='LC22'><span class="c">#   E-Mail:			http://www.google.com/recaptcha/mailhide/d?k=01eb_9W_IYJ4Pm_Y9ALRIPug==&amp;c=L15IEH_kstH8WRWfqnRyeW4IDQuZPzNDRB0KCzMTbHQ=</span></div><div class='line' id='LC23'><span class="c">#</span></div><div class='line' id='LC24'><span class="c">#   Description:		This script will create EA importable files</span></div><div class='line' id='LC25'><span class="c">#                               from .txt (.doc) and .csv (.xls) requirements files</span></div><div class='line' id='LC26'><span class="c">#</span></div><div class='line' id='LC27'><span class="c">#   Limitations:		Error handling is correctly implemented, time constraints</span></div><div class='line' id='LC28'><span class="c">#	The code is not clean and elegant as it should, again, time constraints</span></div><div class='line' id='LC29'><span class="c">#   Database tables used:	None </span></div><div class='line' id='LC30'><span class="c">#   Thread Safe:	        No</span></div><div class='line' id='LC31'><span class="c">#   Extendable:			No</span></div><div class='line' id='LC32'><span class="c">#   Platform Dependencies:	Linux (openSUSE used)</span></div><div class='line' id='LC33'><span class="c">#   Compiler Options:</span></div><div class='line' id='LC34'><br/></div><div class='line' id='LC35'><span class="kn">import</span> <span class="nn">unittest</span></div><div class='line' id='LC36'><span class="kn">import</span> <span class="nn">random</span></div><div class='line' id='LC37'><span class="kn">import</span> <span class="nn">sys</span></div><div class='line' id='LC38'><span class="kn">import</span> <span class="nn">inspect</span></div><div class='line' id='LC39'><span class="kn">import</span> <span class="nn">codecs</span></div><div class='line' id='LC40'><span class="kn">import</span> <span class="nn">csv</span></div><div class='line' id='LC41'><span class="kn">import</span> <span class="nn">reqbox.lib.rbstrlib</span> <span class="kn">as</span> <span class="nn">strlib</span></div><div class='line' id='LC42'><br/></div><div class='line' id='LC43'><span class="k">class</span> <span class="nc">ReqBoxTest</span><span class="p">():</span></div><div class='line' id='LC44'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; Reqbox</span></div><div class='line' id='LC45'><span class="sd">    Attributes:</span></div><div class='line' id='LC46'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC49'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Public</span></div><div class='line' id='LC50'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Init structures</span></div><div class='line' id='LC51'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rb</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">initobject</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">rb</span><span class="p">):</span><span class="c">#, ParserClass):</span></div><div class='line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">rb</span> <span class="o">=</span> <span class="n">rb</span></div><div class='line' id='LC56'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">test01</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; Test01: UC number missing</span></div><div class='line' id='LC59'><span class="sd">        Type: offline</span></div><div class='line' id='LC60'><span class="sd">        Attributes:</span></div><div class='line' id='LC61'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">itemsnumber</span> <span class="o">=</span> <span class="n">rb</span><span class="o">.</span><span class="n">model</span></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC64'><br/></div><div class='line' id='LC65'><br/></div><div class='line' id='LC66'><span class="c"># Verificar se há funcionalidade sem um código UC.</span></div><div class='line' id='LC67'><span class="c">#   ok: not going to happen</span></div><div class='line' id='LC68'><br/></div><div class='line' id='LC69'><span class="c"># Verificar se aparece o mesmo UC mais de uma vez no documento de funcionalidades;</span></div><div class='line' id='LC70'><span class="c"># Verificar se há o mesmo número de UC com nome diferente no documento de funcionalidades.</span></div><div class='line' id='LC71'><span class="c">#   ok: getfundict (assert)</span></div><div class='line' id='LC72'><br/></div><div class='line' id='LC73'><span class="c"># Verificar se aparece o mesmo RFI mais de uma vez no documento de funcionalidades;</span></div><div class='line' id='LC74'><span class="c"># Verificar se há o mesmo número de RFI com nome diferente no documento de funcionalidades.</span></div><div class='line' id='LC75'><span class="c"># Verificar se há o mesmo número de RFN com nome diferente no documento de funcionalidades.</span></div><div class='line' id='LC76'><br/></div><div class='line' id='LC77'><span class="n">rb</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC78'><br/></div><div class='line' id='LC79'><span class="c"># Verificar se tem UC sem utilização;</span></div><div class='line' id='LC80'><span class="c">#   ok: test_parser_missing_01_uc_objects</span></div><div class='line' id='LC81'><span class="c"># Verificar se tem RFI sem utilização;</span></div><div class='line' id='LC82'><span class="c">#   ok: test_parser_missing_02_rfi_objects</span></div><div class='line' id='LC83'><span class="c"># Verificar se tem RFN sem utilização;</span></div><div class='line' id='LC84'><span class="c">#   ok: test_parser_missing_03_rfn_objects</span></div><div class='line' id='LC85'><span class="k">class</span> <span class="nc">TestMissingObjects</span><span class="p">(</span><span class="n">unittest</span><span class="o">.</span><span class="n">TestCase</span><span class="p">):</span></div><div class='line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; </span></div><div class='line' id='LC87'><span class="sd">    Attributes:</span></div><div class='line' id='LC88'><span class="sd">        - rb: ReqBox</span></div><div class='line' id='LC89'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC90'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rb</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC91'><br/></div><div class='line' id='LC92'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setUp</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">rb</span> <span class="o">=</span> <span class="n">rb</span></div><div class='line' id='LC94'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#self.seq = range(10)</span></div><div class='line' id='LC95'><br/></div><div class='line' id='LC96'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#def uckeymeasure(self, key):</span></div><div class='line' id='LC97'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#    #result = self.rb.model.fp.fundict[key][1:] #and key</span></div><div class='line' id='LC98'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#    result = key #and key</span></div><div class='line' id='LC99'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#    return result</span></div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">tag_check</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">filename</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">tagstr</span><span class="p">):</span></div><div class='line' id='LC102'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC103'><span class="sd">        Verifica se foi pulado algum tagstr no dict d e guarda os resultados</span></div><div class='line' id='LC104'><span class="sd">        no arquivo filename</span></div><div class='line' id='LC105'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fh</span> <span class="o">=</span> <span class="n">codecs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s">&#39;utf-8&#39;</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="s">&#39;w&#39;</span><span class="p">)</span> <span class="c"># open(filename, &#39;r&#39;)</span></div><div class='line' id='LC107'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">csvhdlr</span> <span class="o">=</span> <span class="n">csv</span><span class="o">.</span><span class="n">writer</span><span class="p">(</span><span class="n">fh</span><span class="p">,</span> <span class="n">delimiter</span><span class="o">=</span><span class="s">&#39;</span><span class="se">\t</span><span class="s">&#39;</span><span class="p">)</span><span class="c">#, quotechar=&#39;&quot;&#39;)#, quoting=csv.QUOTE_MINIMAL)</span></div><div class='line' id='LC108'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC109'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">itemscount</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">d</span><span class="p">)</span></div><div class='line' id='LC110'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">maxid</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">d</span><span class="p">)</span></div><div class='line' id='LC111'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">maxid</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">tagstr</span><span class="p">):</span></div><div class='line' id='LC112'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">maxid</span> <span class="o">=</span> <span class="n">maxid</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">tagstr</span><span class="p">):]</span></div><div class='line' id='LC113'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#item = max(d, key=self.uckeymeasure)</span></div><div class='line' id='LC114'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#maxid = max(self.uckeymeasure(k) for k in d.keys())</span></div><div class='line' id='LC115'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">csvhdlr</span><span class="o">.</span><span class="n">writerow</span><span class="p">([</span><span class="s">&quot;ID&quot;</span><span class="p">,</span> <span class="s">&quot;Tipo&quot;</span><span class="p">,</span> <span class="s">&quot;Pulados&quot;</span><span class="p">])</span></div><div class='line' id='LC116'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">number</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="nb">int</span><span class="p">(</span><span class="n">maxid</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span><span class="p">):</span></div><div class='line' id='LC117'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">item</span> <span class="o">=</span> <span class="n">tagstr</span> <span class="o">+</span> <span class="s">&#39;</span><span class="si">%03d</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">number</span></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">reqid</span> <span class="o">=</span> <span class="n">item</span></div><div class='line' id='LC119'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">reqname</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></div><div class='line' id='LC120'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">reqtype</span> <span class="o">=</span> <span class="n">tagstr</span></div><div class='line' id='LC121'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">reqbody</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></div><div class='line' id='LC122'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">assertIn</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="n">d</span><span class="p">)</span></div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">status</span> <span class="o">=</span> <span class="s">&#39;ok&#39;</span></div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span><span class="p">:</span></div><div class='line' id='LC126'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">status</span> <span class="o">=</span> <span class="s">&#39;FAILED&#39;</span></div><div class='line' id='LC127'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">rb</span><span class="o">.</span><span class="n">stricttests</span><span class="p">:</span></div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">row</span> <span class="o">=</span> <span class="p">[</span><span class="n">reqid</span><span class="p">,</span> <span class="n">reqtype</span><span class="p">,</span> <span class="n">status</span><span class="p">]</span></div><div class='line' id='LC130'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">csvhdlr</span><span class="o">.</span><span class="n">writerow</span><span class="p">(</span><span class="n">row</span><span class="p">)</span></div><div class='line' id='LC131'><br/></div><div class='line' id='LC132'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">test_parser_0101_missing_uc_objects</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC134'><span class="sd">        Verifica se foi pulado algum numero de UC na sequencia</span></div><div class='line' id='LC135'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC136'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">_getframe</span><span class="p">()</span><span class="o">.</span><span class="n">f_code</span><span class="o">.</span><span class="n">co_name</span> <span class="o">+</span> <span class="s">&#39;.csv&#39;</span></div><div class='line' id='LC137'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">d</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">rb</span><span class="o">.</span><span class="n">model</span><span class="o">.</span><span class="n">fp</span><span class="o">.</span><span class="n">fundict</span></div><div class='line' id='LC138'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tagstr</span> <span class="o">=</span> <span class="s">&#39;UC&#39;</span></div><div class='line' id='LC139'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">tag_check</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">tagstr</span><span class="p">)</span></div><div class='line' id='LC140'><br/></div><div class='line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">test_parser_0102_missing_rfi_objects</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC143'><span class="sd">        Verifica se foi pulado algum numero de RFI na sequencia</span></div><div class='line' id='LC144'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">_getframe</span><span class="p">()</span><span class="o">.</span><span class="n">f_code</span><span class="o">.</span><span class="n">co_name</span> <span class="o">+</span> <span class="s">&#39;.csv&#39;</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">d</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">rb</span><span class="o">.</span><span class="n">model</span><span class="o">.</span><span class="n">uniquerfi</span></div><div class='line' id='LC147'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tagstr</span> <span class="o">=</span> <span class="s">&#39;RFI&#39;</span></div><div class='line' id='LC148'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">tag_check</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">tagstr</span><span class="p">)</span></div><div class='line' id='LC149'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC150'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">test_parser_0103_missing_rfn_objects</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC151'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC152'><span class="sd">        Verifica se foi pulado algum numero de RFN na sequencia</span></div><div class='line' id='LC153'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC154'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">_getframe</span><span class="p">()</span><span class="o">.</span><span class="n">f_code</span><span class="o">.</span><span class="n">co_name</span> <span class="o">+</span> <span class="s">&#39;.csv&#39;</span></div><div class='line' id='LC155'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">d</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">rb</span><span class="o">.</span><span class="n">model</span><span class="o">.</span><span class="n">uniquerfn</span></div><div class='line' id='LC156'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tagstr</span> <span class="o">=</span> <span class="s">&#39;RFN&#39;</span></div><div class='line' id='LC157'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">tag_check</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">tagstr</span><span class="p">)</span></div><div class='line' id='LC158'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC159'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">test_parser_0104_missing_rgn_objects</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC160'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC161'><span class="sd">        Verifica se foi pulado algum numero de RGN na sequencia</span></div><div class='line' id='LC162'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC163'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">_getframe</span><span class="p">()</span><span class="o">.</span><span class="n">f_code</span><span class="o">.</span><span class="n">co_name</span> <span class="o">+</span> <span class="s">&#39;.csv&#39;</span></div><div class='line' id='LC164'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">d</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">rb</span><span class="o">.</span><span class="n">model</span><span class="o">.</span><span class="n">uniquergn</span></div><div class='line' id='LC165'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tagstr</span> <span class="o">=</span> <span class="s">&#39;RGN&#39;</span></div><div class='line' id='LC166'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">tag_check</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">tagstr</span><span class="p">)</span></div><div class='line' id='LC167'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC168'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">test_parser_0105_missing_rnf_objects</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC169'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC170'><span class="sd">        Verifica se foi pulado algum numero de RNF na sequencia</span></div><div class='line' id='LC171'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC172'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">_getframe</span><span class="p">()</span><span class="o">.</span><span class="n">f_code</span><span class="o">.</span><span class="n">co_name</span> <span class="o">+</span> <span class="s">&#39;.csv&#39;</span></div><div class='line' id='LC173'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">d</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">rb</span><span class="o">.</span><span class="n">model</span><span class="o">.</span><span class="n">uniquernf</span></div><div class='line' id='LC174'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tagstr</span> <span class="o">=</span> <span class="s">&#39;RNF&#39;</span></div><div class='line' id='LC175'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">tag_check</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">tagstr</span><span class="p">)</span></div><div class='line' id='LC176'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC177'><span class="k">class</span> <span class="nc">TestOrphanObjects</span><span class="p">(</span><span class="n">unittest</span><span class="o">.</span><span class="n">TestCase</span><span class="p">):</span></div><div class='line' id='LC178'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; </span></div><div class='line' id='LC179'><span class="sd">    Attributes:</span></div><div class='line' id='LC180'><span class="sd">        - rb: ReqBox</span></div><div class='line' id='LC181'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC182'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rb</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC183'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">revrfi</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC184'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">revrfn</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC185'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">revrgn</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC186'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">revrnf</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC187'><br/></div><div class='line' id='LC188'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setUp</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC189'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">rb</span> <span class="o">=</span> <span class="n">rb</span></div><div class='line' id='LC190'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#self.seq = range(10)</span></div><div class='line' id='LC191'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC192'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">reverse_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">get_req_callback</span><span class="p">,</span> <span class="n">set_req_callback</span><span class="p">,</span> <span class="n">d</span><span class="p">):</span></div><div class='line' id='LC193'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fundict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">rb</span><span class="o">.</span><span class="n">model</span><span class="o">.</span><span class="n">fp</span><span class="o">.</span><span class="n">fundict</span></div><div class='line' id='LC194'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">fid</span><span class="p">,</span> <span class="n">funstr</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="nb">sorted</span><span class="p">(</span><span class="n">fundict</span><span class="p">)):</span></div><div class='line' id='LC195'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">funmodel</span> <span class="o">=</span> <span class="n">fundict</span><span class="p">[</span><span class="n">funstr</span><span class="p">]</span></div><div class='line' id='LC196'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">reqdict</span> <span class="o">=</span> <span class="n">get_req_callback</span><span class="p">(</span><span class="n">funmodel</span><span class="p">)</span></div><div class='line' id='LC197'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">rid</span><span class="p">,</span> <span class="n">reqstr</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="nb">sorted</span><span class="p">(</span><span class="n">reqdict</span><span class="p">)):</span></div><div class='line' id='LC198'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">reqmodel</span> <span class="o">=</span> <span class="n">reqdict</span><span class="p">[</span><span class="n">reqstr</span><span class="p">]</span></div><div class='line' id='LC199'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">set_req_callback</span><span class="p">(</span><span class="n">funmodel</span><span class="p">,</span> <span class="n">reqmodel</span><span class="p">,</span> <span class="n">d</span><span class="p">)</span></div><div class='line' id='LC200'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#req = reqdict[reqstr]</span></div><div class='line' id='LC201'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#reqid = reqstr.decode(&#39;utf-8&#39;)</span></div><div class='line' id='LC202'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#reqname = &#39;&#39;</span></div><div class='line' id='LC203'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#if req.reqname is not None:</span></div><div class='line' id='LC204'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#    reqname = req.reqname.encode(&#39;utf-8&#39;)</span></div><div class='line' id='LC205'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#reqbody = &#39;&#39;</span></div><div class='line' id='LC206'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#if req.reqbody is not None:</span></div><div class='line' id='LC207'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#    reqbody = req.reqbody.encode(&#39;utf-8&#39;)</span></div><div class='line' id='LC208'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC209'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC210'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_rfi_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">funmodel</span><span class="p">):</span></div><div class='line' id='LC211'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">funmodel</span><span class="o">.</span><span class="n">rfi</span></div><div class='line' id='LC212'>&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC213'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_rfn_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">funmodel</span><span class="p">):</span></div><div class='line' id='LC214'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">funmodel</span><span class="o">.</span><span class="n">rfn</span></div><div class='line' id='LC215'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC216'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_rgn_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">funmodel</span><span class="p">):</span></div><div class='line' id='LC217'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">funmodel</span><span class="o">.</span><span class="n">rgn</span></div><div class='line' id='LC218'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC219'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_rnf_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">funmodel</span><span class="p">):</span></div><div class='line' id='LC220'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">funmodel</span><span class="o">.</span><span class="n">rnf</span></div><div class='line' id='LC221'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC222'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">set_rev_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fun</span><span class="p">,</span> <span class="n">req</span><span class="p">,</span> <span class="n">d</span><span class="p">):</span></div><div class='line' id='LC223'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#d = self.revrfn</span></div><div class='line' id='LC224'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">req</span><span class="o">.</span><span class="n">reqid</span> <span class="ow">in</span> <span class="n">d</span><span class="p">:</span></div><div class='line' id='LC225'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">d</span><span class="p">[</span><span class="n">req</span><span class="o">.</span><span class="n">reqid</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">fun</span><span class="p">]</span></div><div class='line' id='LC226'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC227'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">l</span> <span class="o">=</span> <span class="n">d</span><span class="p">[</span><span class="n">req</span><span class="o">.</span><span class="n">reqid</span><span class="p">]</span></div><div class='line' id='LC228'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">l</span> <span class="o">+=</span> <span class="p">[</span><span class="n">fun</span><span class="p">]</span></div><div class='line' id='LC229'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC230'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">orphan_check</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">filename</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">tagstr</span><span class="p">):</span></div><div class='line' id='LC231'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fh</span> <span class="o">=</span> <span class="n">codecs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s">&#39;utf-8&#39;</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="s">&#39;w&#39;</span><span class="p">)</span> <span class="c"># open(filename, &#39;r&#39;)</span></div><div class='line' id='LC232'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">csvhdlr</span> <span class="o">=</span> <span class="n">csv</span><span class="o">.</span><span class="n">writer</span><span class="p">(</span><span class="n">fh</span><span class="p">,</span> <span class="n">delimiter</span><span class="o">=</span><span class="s">&#39;</span><span class="se">\t</span><span class="s">&#39;</span><span class="p">)</span><span class="c">#, quotechar=&#39;&quot;&#39;)#, quoting=csv.QUOTE_MINIMAL)</span></div><div class='line' id='LC233'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC234'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">itemscount</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">d</span><span class="p">)</span></div><div class='line' id='LC235'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">maxid</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">d</span><span class="p">)</span></div><div class='line' id='LC236'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">maxid</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">tagstr</span><span class="p">):</span></div><div class='line' id='LC237'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">maxid</span> <span class="o">=</span> <span class="n">maxid</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">tagstr</span><span class="p">):]</span></div><div class='line' id='LC238'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC239'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">csvhdlr</span><span class="o">.</span><span class="n">writerow</span><span class="p">([</span><span class="s">&quot;ID&quot;</span><span class="p">,</span> <span class="s">&quot;Type&quot;</span><span class="p">,</span> <span class="s">&quot;Status&quot;</span><span class="p">])</span></div><div class='line' id='LC240'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">number</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="nb">int</span><span class="p">(</span><span class="n">maxid</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span><span class="p">):</span></div><div class='line' id='LC241'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">item</span> <span class="o">=</span> <span class="n">tagstr</span> <span class="o">+</span> <span class="s">&#39;</span><span class="si">%03d</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">number</span></div><div class='line' id='LC242'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">reqid</span> <span class="o">=</span> <span class="n">item</span></div><div class='line' id='LC243'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">reqname</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></div><div class='line' id='LC244'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">reqtype</span> <span class="o">=</span> <span class="n">tagstr</span></div><div class='line' id='LC245'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">reqbody</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></div><div class='line' id='LC246'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC247'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">assertIn</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="n">d</span><span class="p">)</span></div><div class='line' id='LC248'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">l</span> <span class="o">=</span> <span class="n">d</span><span class="p">[</span><span class="n">item</span><span class="p">]</span></div><div class='line' id='LC249'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">assertNotEqual</span><span class="p">(</span><span class="n">l</span><span class="p">,</span> <span class="p">[])</span></div><div class='line' id='LC250'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">status</span> <span class="o">=</span> <span class="s">&#39;ok&#39;</span></div><div class='line' id='LC251'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span><span class="p">:</span></div><div class='line' id='LC252'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">status</span> <span class="o">=</span> <span class="s">&#39;FAILED&#39;</span></div><div class='line' id='LC253'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">rb</span><span class="o">.</span><span class="n">stricttests</span><span class="p">:</span></div><div class='line' id='LC254'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span></div><div class='line' id='LC255'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">row</span> <span class="o">=</span> <span class="p">[</span><span class="n">reqid</span><span class="p">,</span> <span class="n">reqtype</span><span class="p">,</span> <span class="n">status</span><span class="p">]</span></div><div class='line' id='LC256'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">csvhdlr</span><span class="o">.</span><span class="n">writerow</span><span class="p">(</span><span class="n">row</span><span class="p">)</span></div><div class='line' id='LC257'><br/></div><div class='line' id='LC258'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">test_parser_0201_orphan_rfi_objects</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC259'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">_getframe</span><span class="p">()</span><span class="o">.</span><span class="n">f_code</span><span class="o">.</span><span class="n">co_name</span> <span class="o">+</span> <span class="s">&#39;.csv&#39;</span></div><div class='line' id='LC260'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">d</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">revrfi</span></div><div class='line' id='LC261'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tagstr</span> <span class="o">=</span> <span class="s">&#39;RFI&#39;</span></div><div class='line' id='LC262'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">reverse_dict</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_rfi_dict</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">set_rev_dict</span><span class="p">,</span> <span class="n">d</span><span class="p">)</span></div><div class='line' id='LC263'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">orphan_check</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">tagstr</span><span class="p">)</span></div><div class='line' id='LC264'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC265'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">test_parser_0202_orphan_rfn_objects</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC266'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">_getframe</span><span class="p">()</span><span class="o">.</span><span class="n">f_code</span><span class="o">.</span><span class="n">co_name</span> <span class="o">+</span> <span class="s">&#39;.csv&#39;</span></div><div class='line' id='LC267'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">d</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">revrfn</span></div><div class='line' id='LC268'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tagstr</span> <span class="o">=</span> <span class="s">&#39;RFN&#39;</span></div><div class='line' id='LC269'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">reverse_dict</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_rfn_dict</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">set_rev_dict</span><span class="p">,</span> <span class="n">d</span><span class="p">)</span></div><div class='line' id='LC270'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">orphan_check</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">tagstr</span><span class="p">)</span></div><div class='line' id='LC271'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC272'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">test_parser_0203_orphan_rgn_objects</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC273'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">_getframe</span><span class="p">()</span><span class="o">.</span><span class="n">f_code</span><span class="o">.</span><span class="n">co_name</span> <span class="o">+</span> <span class="s">&#39;.csv&#39;</span></div><div class='line' id='LC274'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">d</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">revrgn</span></div><div class='line' id='LC275'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tagstr</span> <span class="o">=</span> <span class="s">&#39;RGN&#39;</span></div><div class='line' id='LC276'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">reverse_dict</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_rgn_dict</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">set_rev_dict</span><span class="p">,</span> <span class="n">d</span><span class="p">)</span></div><div class='line' id='LC277'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">orphan_check</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">tagstr</span><span class="p">)</span></div><div class='line' id='LC278'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC279'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">test_parser_0204_orphan_rnf_objects</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC280'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">_getframe</span><span class="p">()</span><span class="o">.</span><span class="n">f_code</span><span class="o">.</span><span class="n">co_name</span> <span class="o">+</span> <span class="s">&#39;.csv&#39;</span></div><div class='line' id='LC281'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">d</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">revrnf</span></div><div class='line' id='LC282'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tagstr</span> <span class="o">=</span> <span class="s">&#39;RNF&#39;</span></div><div class='line' id='LC283'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">reverse_dict</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_rnf_dict</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">set_rev_dict</span><span class="p">,</span> <span class="n">d</span><span class="p">)</span></div><div class='line' id='LC284'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">orphan_check</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">tagstr</span><span class="p">)</span></div><div class='line' id='LC285'><br/></div><div class='line' id='LC286'><span class="c"># Verificar se há caso de uso que não é extendido nem implementado por ninguém.</span></div><div class='line' id='LC287'><span class="c">#   Subdividido em dois</span></div><div class='line' id='LC288'><span class="c">#       Extends: test_parser_rel_missing_01_uc_extends</span></div><div class='line' id='LC289'><span class="c">#       Includes test_parser_rel_missing_02_uc_includes</span></div><div class='line' id='LC290'><span class="c"># TODO: Perhaps I need to reverse the dictionaries to do the same check</span></div><div class='line' id='LC291'><span class="k">class</span> <span class="nc">TestOrphanUCRel</span><span class="p">(</span><span class="n">unittest</span><span class="o">.</span><span class="n">TestCase</span><span class="p">):</span></div><div class='line' id='LC292'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; </span></div><div class='line' id='LC293'><span class="sd">    Attributes:</span></div><div class='line' id='LC294'><span class="sd">        - rb: ReqBox</span></div><div class='line' id='LC295'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC296'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rb</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC297'><br/></div><div class='line' id='LC298'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setUp</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC299'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">rb</span> <span class="o">=</span> <span class="n">rb</span></div><div class='line' id='LC300'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#self.seq = range(10)</span></div><div class='line' id='LC301'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC302'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_ext_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">funmodel</span><span class="p">):</span></div><div class='line' id='LC303'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">funmodel</span><span class="o">.</span><span class="n">extends</span></div><div class='line' id='LC304'>&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC305'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_inc_dict</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">funmodel</span><span class="p">):</span></div><div class='line' id='LC306'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">funmodel</span><span class="o">.</span><span class="n">includes</span></div><div class='line' id='LC307'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC308'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">orphan_check</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">filename</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">tagstr</span><span class="p">,</span> <span class="n">get_dict_callback</span><span class="p">):</span></div><div class='line' id='LC309'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fh</span> <span class="o">=</span> <span class="n">codecs</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s">&#39;utf-8&#39;</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="s">&#39;w&#39;</span><span class="p">)</span> <span class="c"># open(filename, &#39;r&#39;)</span></div><div class='line' id='LC310'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">csvhdlr</span> <span class="o">=</span> <span class="n">csv</span><span class="o">.</span><span class="n">writer</span><span class="p">(</span><span class="n">fh</span><span class="p">,</span> <span class="n">delimiter</span><span class="o">=</span><span class="s">&#39;</span><span class="se">\t</span><span class="s">&#39;</span><span class="p">)</span><span class="c">#, quotechar=&#39;&quot;&#39;)#, quoting=csv.QUOTE_MINIMAL)</span></div><div class='line' id='LC311'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC312'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">itemscount</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">d</span><span class="p">)</span></div><div class='line' id='LC313'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">maxid</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">d</span><span class="p">)</span></div><div class='line' id='LC314'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">maxid</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">tagstr</span><span class="p">):</span></div><div class='line' id='LC315'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">maxid</span> <span class="o">=</span> <span class="n">maxid</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">tagstr</span><span class="p">):]</span></div><div class='line' id='LC316'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC317'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">csvhdlr</span><span class="o">.</span><span class="n">writerow</span><span class="p">([</span><span class="s">&quot;ID&quot;</span><span class="p">,</span> <span class="s">&quot;Type&quot;</span><span class="p">,</span> <span class="s">&quot;Status&quot;</span><span class="p">])</span></div><div class='line' id='LC318'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">number</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="nb">int</span><span class="p">(</span><span class="n">maxid</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span><span class="p">):</span></div><div class='line' id='LC319'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">item</span> <span class="o">=</span> <span class="n">tagstr</span> <span class="o">+</span> <span class="s">&#39;</span><span class="si">%03d</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">number</span></div><div class='line' id='LC320'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">reqid</span> <span class="o">=</span> <span class="n">item</span></div><div class='line' id='LC321'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">reqname</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></div><div class='line' id='LC322'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">reqtype</span> <span class="o">=</span> <span class="n">tagstr</span></div><div class='line' id='LC323'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">reqbody</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></div><div class='line' id='LC324'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC325'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">assertIn</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="n">d</span><span class="p">)</span></div><div class='line' id='LC326'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">uc</span> <span class="o">=</span> <span class="n">d</span><span class="p">[</span><span class="n">item</span><span class="p">]</span></div><div class='line' id='LC327'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">subdict</span> <span class="o">=</span> <span class="n">get_dict_callback</span><span class="p">(</span><span class="n">uc</span><span class="p">)</span></div><div class='line' id='LC328'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">assertNotEqual</span><span class="p">(</span><span class="n">subdict</span><span class="p">,</span> <span class="p">{})</span></div><div class='line' id='LC329'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">status</span> <span class="o">=</span> <span class="s">&#39;ok&#39;</span></div><div class='line' id='LC330'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span><span class="p">:</span></div><div class='line' id='LC331'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">status</span> <span class="o">=</span> <span class="s">&#39;FAILED&#39;</span></div><div class='line' id='LC332'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">rb</span><span class="o">.</span><span class="n">stricttests</span><span class="p">:</span></div><div class='line' id='LC333'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span></div><div class='line' id='LC334'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">row</span> <span class="o">=</span> <span class="p">[</span><span class="n">reqid</span><span class="p">,</span> <span class="n">reqtype</span><span class="p">,</span> <span class="n">status</span><span class="p">]</span></div><div class='line' id='LC335'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">csvhdlr</span><span class="o">.</span><span class="n">writerow</span><span class="p">(</span><span class="n">row</span><span class="p">)</span></div><div class='line' id='LC336'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC337'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">test_parser_0301_rel_missing_uc_extends</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC338'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">_getframe</span><span class="p">()</span><span class="o">.</span><span class="n">f_code</span><span class="o">.</span><span class="n">co_name</span> <span class="o">+</span> <span class="s">&#39;.csv&#39;</span></div><div class='line' id='LC339'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">d</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">rb</span><span class="o">.</span><span class="n">model</span><span class="o">.</span><span class="n">fp</span><span class="o">.</span><span class="n">fundict</span></div><div class='line' id='LC340'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">orphan_check</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="s">&#39;UC&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_ext_dict</span><span class="p">)</span></div><div class='line' id='LC341'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC342'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">test_parser_0302_rel_missing_uc_includes</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC343'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">_getframe</span><span class="p">()</span><span class="o">.</span><span class="n">f_code</span><span class="o">.</span><span class="n">co_name</span> <span class="o">+</span> <span class="s">&#39;.csv&#39;</span></div><div class='line' id='LC344'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">d</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">rb</span><span class="o">.</span><span class="n">model</span><span class="o">.</span><span class="n">fp</span><span class="o">.</span><span class="n">fundict</span></div><div class='line' id='LC345'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">orphan_check</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="s">&#39;UC&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_inc_dict</span><span class="p">)</span></div><div class='line' id='LC346'><br/></div><div class='line' id='LC347'><span class="c"># Verificar se há o mesmo nome de UC com número diferente no documento de funcionalidades.</span></div><div class='line' id='LC348'><span class="c">#   ok: test_parser_0401_fuzzy_reqstr_uc</span></div><div class='line' id='LC349'><span class="c"># Verificar se há o mesmo nome de RFI com número diferente no documento de funcionalidades.</span></div><div class='line' id='LC350'><span class="c">#   ok: test_parser_0402_fuzzy_reqstr_rfi</span></div><div class='line' id='LC351'><span class="c"># Verificar se há o mesmo nome de RFN com número diferente no documento de funcionalidades.</span></div><div class='line' id='LC352'><span class="c">#   ok: test_parser_0403_fuzzy_reqstr_rfn</span></div><div class='line' id='LC353'><span class="k">class</span> <span class="nc">TestFuzzyStrMatch</span><span class="p">(</span><span class="n">unittest</span><span class="o">.</span><span class="n">TestCase</span><span class="p">):</span></div><div class='line' id='LC354'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; </span></div><div class='line' id='LC355'><span class="sd">    Attributes:</span></div><div class='line' id='LC356'><span class="sd">        - rb: ReqBox</span></div><div class='line' id='LC357'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC358'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rb</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC359'><br/></div><div class='line' id='LC360'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setUp</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC361'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">rb</span> <span class="o">=</span> <span class="n">rb</span></div><div class='line' id='LC362'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#self.seq = range(10)</span></div><div class='line' id='LC363'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC364'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_uc_str</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">funmodel</span><span class="p">):</span></div><div class='line' id='LC365'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">funmodel</span><span class="o">.</span><span class="n">fun</span><span class="o">.</span><span class="n">reqname</span></div><div class='line' id='LC366'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC367'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_reqname</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">funmodel</span><span class="p">):</span></div><div class='line' id='LC368'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">funmodel</span><span class="o">.</span><span class="n">reqname</span></div><div class='line' id='LC369'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC370'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">fuzzy_str_match_iterate</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">itemstr</span><span class="p">,</span> <span class="n">getter</span><span class="p">):</span></div><div class='line' id='LC371'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ratio</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC372'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC373'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">funstr</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></div><div class='line' id='LC374'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">d</span><span class="p">:</span></div><div class='line' id='LC375'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">s1</span> <span class="o">=</span> <span class="n">getter</span><span class="p">(</span><span class="n">d</span><span class="p">[</span><span class="n">i</span><span class="p">])</span></div><div class='line' id='LC376'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#s2 = getter(item)</span></div><div class='line' id='LC377'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ratioeval</span> <span class="o">=</span> <span class="n">strlib</span><span class="o">.</span><span class="n">mystrfuzzycmp</span><span class="p">(</span><span class="n">s1</span><span class="p">,</span> <span class="n">itemstr</span><span class="p">)</span></div><div class='line' id='LC378'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">itemstr</span> <span class="o">!=</span> <span class="n">s1</span> <span class="ow">and</span> <span class="n">ratioeval</span> <span class="o">&gt;</span> <span class="n">ratio</span><span class="p">:</span></div><div class='line' id='LC379'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result</span> <span class="o">=</span> <span class="n">i</span></div><div class='line' id='LC380'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ratio</span> <span class="o">=</span> <span class="n">ratioeval</span></div><div class='line' id='LC381'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">funstr</span> <span class="o">=</span> <span class="n">s1</span></div><div class='line' id='LC382'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">ratio</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="n">funstr</span></div><div class='line' id='LC383'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC384'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">fuzzy_str_match</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">filename</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">tagstr</span><span class="p">,</span> <span class="n">getter</span><span class="p">):</span></div><div class='line' id='LC385'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fh</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="s">&#39;wb&#39;</span><span class="p">)</span></div><div class='line' id='LC386'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#fh = codecs.open(filename, encoding=&#39;latin1&#39;, mode=&#39;w&#39;) # open(filename, &#39;r&#39;)</span></div><div class='line' id='LC387'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">csvhdlr</span> <span class="o">=</span> <span class="n">csv</span><span class="o">.</span><span class="n">writer</span><span class="p">(</span><span class="n">fh</span><span class="p">,</span> <span class="n">delimiter</span><span class="o">=</span><span class="s">&#39;</span><span class="se">\t</span><span class="s">&#39;</span><span class="p">)</span><span class="c">#, quotechar=&#39;&quot;&#39;)#, quoting=csv.QUOTE_MINIMAL)</span></div><div class='line' id='LC388'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC389'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">itemscount</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">d</span><span class="p">)</span></div><div class='line' id='LC390'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">maxid</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">d</span><span class="p">)</span></div><div class='line' id='LC391'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">maxid</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">tagstr</span><span class="p">):</span></div><div class='line' id='LC392'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">maxid</span> <span class="o">=</span> <span class="n">maxid</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">tagstr</span><span class="p">):]</span></div><div class='line' id='LC393'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC394'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">csvhdlr</span><span class="o">.</span><span class="n">writerow</span><span class="p">([</span><span class="s">&quot;ID&quot;</span><span class="p">,</span> <span class="s">&quot;Title&quot;</span><span class="p">,</span> <span class="s">&quot;Type&quot;</span><span class="p">,</span> <span class="s">&quot;Ratio&quot;</span><span class="p">,</span> <span class="s">&quot;ID&quot;</span><span class="p">,</span> <span class="s">&quot;Title&quot;</span><span class="p">])</span></div><div class='line' id='LC395'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">number</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="nb">int</span><span class="p">(</span><span class="n">maxid</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span><span class="p">):</span></div><div class='line' id='LC396'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">item</span> <span class="o">=</span> <span class="n">tagstr</span> <span class="o">+</span> <span class="s">&#39;</span><span class="si">%03d</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">number</span></div><div class='line' id='LC397'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">reqid</span> <span class="o">=</span> <span class="n">item</span></div><div class='line' id='LC398'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">reqname</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></div><div class='line' id='LC399'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">reqtype</span> <span class="o">=</span> <span class="n">tagstr</span></div><div class='line' id='LC400'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">reqbody</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></div><div class='line' id='LC401'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">reqstr</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></div><div class='line' id='LC402'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC403'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">assertIn</span><span class="p">(</span><span class="n">item</span><span class="p">,</span> <span class="n">d</span><span class="p">)</span></div><div class='line' id='LC404'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">reqstr</span> <span class="o">=</span> <span class="n">getter</span><span class="p">(</span><span class="n">d</span><span class="p">[</span><span class="n">item</span><span class="p">])</span></div><div class='line' id='LC405'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#self.assertNotEqual(l, [])</span></div><div class='line' id='LC406'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ratio</span><span class="p">,</span> <span class="n">nearest</span><span class="p">,</span> <span class="n">neareststr</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fuzzy_str_match_iterate</span><span class="p">(</span><span class="n">d</span><span class="p">,</span> <span class="n">reqstr</span><span class="p">,</span> <span class="n">getter</span><span class="p">)</span></div><div class='line' id='LC407'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ratio</span> <span class="o">=</span> <span class="s">&#39;</span><span class="si">%0.2f</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">ratio</span><span class="o">*</span><span class="mi">100</span><span class="p">)</span> <span class="o">+</span><span class="s">&#39;%&#39;</span></div><div class='line' id='LC408'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">status</span> <span class="o">=</span> <span class="s">&#39;ok&#39;</span></div><div class='line' id='LC409'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span><span class="p">:</span></div><div class='line' id='LC410'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">status</span> <span class="o">=</span> <span class="s">&#39;FAILED&#39;</span></div><div class='line' id='LC411'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ratio</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span></div><div class='line' id='LC412'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">nearest</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></div><div class='line' id='LC413'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">neareststr</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></div><div class='line' id='LC414'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">rb</span><span class="o">.</span><span class="n">stricttests</span><span class="p">:</span></div><div class='line' id='LC415'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span></div><div class='line' id='LC416'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#row = [reqid, reqstr.encode(&#39;latin1&#39;), reqtype, ratio, nearest, neareststr.encode(&#39;latin1&#39;)]</span></div><div class='line' id='LC417'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">row</span> <span class="o">=</span> <span class="p">[</span><span class="n">reqid</span><span class="p">,</span> <span class="n">reqstr</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s">&#39;utf-8&#39;</span><span class="p">),</span> <span class="n">reqtype</span><span class="p">,</span> <span class="n">ratio</span><span class="p">,</span> <span class="n">nearest</span><span class="p">,</span> <span class="n">neareststr</span><span class="o">.</span><span class="n">encode</span><span class="p">(</span><span class="s">&#39;utf-8&#39;</span><span class="p">)]</span></div><div class='line' id='LC418'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">csvhdlr</span><span class="o">.</span><span class="n">writerow</span><span class="p">(</span><span class="n">row</span><span class="p">)</span></div><div class='line' id='LC419'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC420'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">test_parser_0401_fuzzy_reqstr_uc</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC421'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">_getframe</span><span class="p">()</span><span class="o">.</span><span class="n">f_code</span><span class="o">.</span><span class="n">co_name</span> <span class="o">+</span> <span class="s">&#39;.csv&#39;</span></div><div class='line' id='LC422'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">d</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">rb</span><span class="o">.</span><span class="n">model</span><span class="o">.</span><span class="n">fp</span><span class="o">.</span><span class="n">fundict</span></div><div class='line' id='LC423'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">fuzzy_str_match</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="s">&#39;UC&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_uc_str</span><span class="p">)</span></div><div class='line' id='LC424'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC425'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">test_parser_0402_fuzzy_reqstr_rfi</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC426'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">_getframe</span><span class="p">()</span><span class="o">.</span><span class="n">f_code</span><span class="o">.</span><span class="n">co_name</span> <span class="o">+</span> <span class="s">&#39;.csv&#39;</span></div><div class='line' id='LC427'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">d</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">rb</span><span class="o">.</span><span class="n">model</span><span class="o">.</span><span class="n">uniquerfi</span></div><div class='line' id='LC428'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">fuzzy_str_match</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="s">&#39;RFI&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_reqname</span><span class="p">)</span></div><div class='line' id='LC429'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC430'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">test_parser_0403_fuzzy_reqstr_rfn</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC431'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">_getframe</span><span class="p">()</span><span class="o">.</span><span class="n">f_code</span><span class="o">.</span><span class="n">co_name</span> <span class="o">+</span> <span class="s">&#39;.csv&#39;</span></div><div class='line' id='LC432'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">d</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">rb</span><span class="o">.</span><span class="n">model</span><span class="o">.</span><span class="n">uniquerfn</span></div><div class='line' id='LC433'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">fuzzy_str_match</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="s">&#39;RFN&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_reqname</span><span class="p">)</span></div><div class='line' id='LC434'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC435'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">test_parser_0404_fuzzy_reqstr_rgn</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC436'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">_getframe</span><span class="p">()</span><span class="o">.</span><span class="n">f_code</span><span class="o">.</span><span class="n">co_name</span> <span class="o">+</span> <span class="s">&#39;.csv&#39;</span></div><div class='line' id='LC437'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">d</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">rb</span><span class="o">.</span><span class="n">model</span><span class="o">.</span><span class="n">uniquergn</span></div><div class='line' id='LC438'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">fuzzy_str_match</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="s">&#39;RGN&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_reqname</span><span class="p">)</span></div><div class='line' id='LC439'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC440'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">test_parser_0405_fuzzy_reqstr_rnf</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC441'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">filename</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">_getframe</span><span class="p">()</span><span class="o">.</span><span class="n">f_code</span><span class="o">.</span><span class="n">co_name</span> <span class="o">+</span> <span class="s">&#39;.csv&#39;</span></div><div class='line' id='LC442'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">d</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">rb</span><span class="o">.</span><span class="n">model</span><span class="o">.</span><span class="n">uniquernf</span></div><div class='line' id='LC443'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">fuzzy_str_match</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="s">&#39;RNF&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_reqname</span><span class="p">)</span></div><div class='line' id='LC444'><br/></div><div class='line' id='LC445'><span class="k">class</span> <span class="nc">TestEAIntegrity</span><span class="p">(</span><span class="n">unittest</span><span class="o">.</span><span class="n">TestCase</span><span class="p">):</span></div><div class='line' id='LC446'><br/></div><div class='line' id='LC447'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">setUp</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC448'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">seq</span> <span class="o">=</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span></div><div class='line' id='LC449'><br/></div><div class='line' id='LC450'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">test_shuffle</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC451'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># make sure the shuffled sequence does not lose any elements</span></div><div class='line' id='LC452'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">random</span><span class="o">.</span><span class="n">shuffle</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">seq</span><span class="p">)</span></div><div class='line' id='LC453'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">seq</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span></div><div class='line' id='LC454'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">assertEqual</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">seq</span><span class="p">,</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">))</span></div><div class='line' id='LC455'><br/></div><div class='line' id='LC456'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># should raise an exception for an immutable sequence</span></div><div class='line' id='LC457'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">assertRaises</span><span class="p">(</span><span class="ne">TypeError</span><span class="p">,</span> <span class="n">random</span><span class="o">.</span><span class="n">shuffle</span><span class="p">,</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">))</span></div><div class='line' id='LC458'><br/></div><div class='line' id='LC459'><span class="k">def</span> <span class="nf">parsingsuite</span><span class="p">():</span></div><div class='line' id='LC460'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#args = sys.argv[1:]</span></div><div class='line' id='LC461'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">suite</span> <span class="o">=</span> <span class="n">unittest</span><span class="o">.</span><span class="n">TestSuite</span><span class="p">()</span></div><div class='line' id='LC462'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">suite</span><span class="o">.</span><span class="n">addTest</span><span class="p">(</span><span class="n">unittest</span><span class="o">.</span><span class="n">makeSuite</span><span class="p">(</span><span class="n">TestMissingObjects</span><span class="p">))</span></div><div class='line' id='LC463'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">suite</span><span class="o">.</span><span class="n">addTest</span><span class="p">(</span><span class="n">unittest</span><span class="o">.</span><span class="n">makeSuite</span><span class="p">(</span><span class="n">TestOrphanObjects</span><span class="p">))</span></div><div class='line' id='LC464'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">suite</span><span class="o">.</span><span class="n">addTest</span><span class="p">(</span><span class="n">unittest</span><span class="o">.</span><span class="n">makeSuite</span><span class="p">(</span><span class="n">TestOrphanUCRel</span><span class="p">))</span></div><div class='line' id='LC465'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">suite</span><span class="o">.</span><span class="n">addTest</span><span class="p">(</span><span class="n">unittest</span><span class="o">.</span><span class="n">makeSuite</span><span class="p">(</span><span class="n">TestFuzzyStrMatch</span><span class="p">))</span></div><div class='line' id='LC466'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">suite</span></div><div class='line' id='LC467'><br/></div><div class='line' id='LC468'><span class="k">def</span> <span class="nf">easuite</span><span class="p">():</span></div><div class='line' id='LC469'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">suite</span> <span class="o">=</span> <span class="n">unittest</span><span class="o">.</span><span class="n">TestSuite</span><span class="p">()</span></div><div class='line' id='LC470'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">suite</span><span class="o">.</span><span class="n">addTest</span><span class="p">(</span><span class="n">unittest</span><span class="o">.</span><span class="n">makeSuite</span><span class="p">(</span><span class="n">TestEAIntegrity</span><span class="p">))</span></div><div class='line' id='LC471'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">suite</span></div><div class='line' id='LC472'><br/></div><div class='line' id='LC473'><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span></div><div class='line' id='LC474'><span class="c">#    unittest.main(verbosity=2)</span></div><div class='line' id='LC475'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC476'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC477'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">suiteFew</span> <span class="o">=</span> <span class="n">unittest</span><span class="o">.</span><span class="n">TestSuite</span><span class="p">()</span></div><div class='line' id='LC478'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#suiteFew.addTest(TestMissingObjects(&quot;test_01_UC_missing&quot;))</span></div><div class='line' id='LC479'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#suiteFew.addTest(TestMissingObjects(&quot;test_shuffle&quot;))</span></div><div class='line' id='LC480'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#unittest.TextTestRunner(verbosity=2).run(suiteFew)</span></div><div class='line' id='LC481'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">unittest</span><span class="o">.</span><span class="n">TextTestRunner</span><span class="p">(</span><span class="n">verbosity</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">parsingsuite</span><span class="p">())</span></div><div class='line' id='LC482'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC483'><span class="c">#suite1 = unittest.TestSuite(MyTestCase1(), MyTestCase2())</span></div><div class='line' id='LC484'><span class="c">#suite2 = unittest.TestSuite()</span></div><div class='line' id='LC485'><span class="c">#suite2.addTest(MyOtherTestCase())</span></div><div class='line' id='LC486'><span class="c">#</span></div><div class='line' id='LC487'><span class="c">#big_suite = unittest.TestSuite(suite1)</span></div><div class='line' id='LC488'><span class="c">#big_suite.addTest(suite2)</span></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>

        <a href="#jump-to-line" rel="facebox" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
        <div id="jump-to-line" style="display:none">
          <h2>Jump to Line</h2>
          <form accept-charset="UTF-8" class="js-jump-to-line-form">
            <input class="textfield js-jump-to-line-field" type="text">
            <div class="full-button">
              <button type="submit" class="button">Go</button>
            </div>
          </form>
        </div>

      </div>
    </div>
</div>

<div id="js-frame-loading-template" class="frame frame-loading large-loading-area" style="display:none;">
  <img class="js-frame-loading-spinner" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-128.gif?1347543525" height="64" width="64">
</div>


        </div>
      </div>
      <div class="modal-backdrop"></div>
    </div>

      <div id="footer-push"></div><!-- hack for sticky footer -->
    </div><!-- end of wrapper - hack for sticky footer -->

      <!-- footer -->
      <div id="footer">
  <div class="container clearfix">

      <dl class="footer_nav">
        <dt>GitHub</dt>
        <dd><a href="https://github.com/about">About us</a></dd>
        <dd><a href="https://github.com/blog">Blog</a></dd>
        <dd><a href="https://github.com/contact">Contact &amp; support</a></dd>
        <dd><a href="http://enterprise.github.com/">GitHub Enterprise</a></dd>
        <dd><a href="http://status.github.com/">Site status</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Applications</dt>
        <dd><a href="http://mac.github.com/">GitHub for Mac</a></dd>
        <dd><a href="http://windows.github.com/">GitHub for Windows</a></dd>
        <dd><a href="http://eclipse.github.com/">GitHub for Eclipse</a></dd>
        <dd><a href="http://mobile.github.com/">GitHub mobile apps</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Services</dt>
        <dd><a href="http://get.gaug.es/">Gauges: Web analytics</a></dd>
        <dd><a href="http://speakerdeck.com">Speaker Deck: Presentations</a></dd>
        <dd><a href="https://gist.github.com">Gist: Code snippets</a></dd>
        <dd><a href="http://jobs.github.com/">Job board</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Documentation</dt>
        <dd><a href="http://help.github.com/">GitHub Help</a></dd>
        <dd><a href="http://developer.github.com/">Developer API</a></dd>
        <dd><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></dd>
        <dd><a href="http://pages.github.com/">GitHub Pages</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>More</dt>
        <dd><a href="http://training.github.com/">Training</a></dd>
        <dd><a href="https://github.com/edu">Students &amp; teachers</a></dd>
        <dd><a href="http://shop.github.com">The Shop</a></dd>
        <dd><a href="https://github.com/plans">Plans &amp; pricing</a></dd>
        <dd><a href="http://octodex.github.com/">The Octodex</a></dd>
      </dl>

      <hr class="footer-divider">


    <p class="right">&copy; 2013 <span title="0.11980s from fe17.rs.github.com">GitHub</span>, Inc. All rights reserved.</p>
    <a class="left" href="https://github.com/">
      <span class="mega-octicon octicon-mark-github"></span>
    </a>
    <ul id="legal">
        <li><a href="https://github.com/site/terms">Terms of Service</a></li>
        <li><a href="https://github.com/site/privacy">Privacy</a></li>
        <li><a href="https://github.com/security">Security</a></li>
    </ul>

  </div><!-- /.container -->

</div><!-- /.#footer -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/vonpupp/siga-tools-doc-reqbox-txt/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      Something went wrong with that request. Please try again.
      <a href="#" class="octicon octicon-remove-close ajax-error-dismiss"></a>
    </div>

    
    
    <span id='server_response_time' data-time='0.12022' data-host='fe17'></span>
    
  </body>
</html>

