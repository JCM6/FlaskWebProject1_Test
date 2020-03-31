#This file contains methods that load html from the API
def loadTestFile():
    with open('FlaskWebProject1_Test\\testLoadFile.html', 'r') as file:
        openHTML = file
    return str(openHTML)

index = loadTestFile()

chunkPage = """
<!DOCTYPE html> 
<!--[if lt IE 7 ]> <html lang="en-US" class="no-js ie6"> <![endif]-->
<!--[if IE 7 ]>    <html lang="en-US" class="no-js ie7"> <![endif]-->
<!--[if IE 8 ]>    <html lang="en-US" class="no-js ie8"> <![endif]-->
<!--[if IE 9 ]>    <html lang="en-US" class="no-js ie9"> <![endif]-->
<!--[if (gt IE 9)|!(IE)]><!--><html lang="en-US" class="no-js"> <!--<![endif]-->

<head profile="http://gmpg.org/xfn/11">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>About LibriVox |  LibriVox   About LibriVox | free public domain audiobooks </title>

<link rel="shortcut icon" href="https://librivox.org/wp-content/themes/librivox/favicon.ico" />
<!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js">
      </script>
    <![endif]-->
<link rel='dns-prefetch' href='//s.w.org' />
<link rel="alternate" type="application/rss+xml" title="LibriVox &raquo; Feed" href="https://librivox.org/feed/" />
<link rel="alternate" type="application/rss+xml" title="LibriVox &raquo; Comments Feed" href="https://librivox.org/comments/feed/" />
<link rel="alternate" type="application/rss+xml" title="LibriVox &raquo; About LibriVox Comments Feed" href="https://librivox.org/pages/about-librivox/feed/" />
		<script type="text/javascript">
			window._wpemojiSettings = {"baseUrl":"https:\/\/s.w.org\/images\/core\/emoji\/12.0.0-1\/72x72\/","ext":".png","svgUrl":"https:\/\/s.w.org\/images\/core\/emoji\/12.0.0-1\/svg\/","svgExt":".svg","source":{"concatemoji":"https:\/\/librivox.org\/wp-includes\/js\/wp-emoji-release.min.js?ver=5.2.3"}};
			!function(a,b,c){function d(a,b){var c=String.fromCharCode;l.clearRect(0,0,k.width,k.height),l.fillText(c.apply(this,a),0,0);var d=k.toDataURL();l.clearRect(0,0,k.width,k.height),l.fillText(c.apply(this,b),0,0);var e=k.toDataURL();return d===e}function e(a){var b;if(!l||!l.fillText)return!1;switch(l.textBaseline="top",l.font="600 32px Arial",a){case"flag":return!(b=d([55356,56826,55356,56819],[55356,56826,8203,55356,56819]))&&(b=d([55356,57332,56128,56423,56128,56418,56128,56421,56128,56430,56128,56423,56128,56447],[55356,57332,8203,56128,56423,8203,56128,56418,8203,56128,56421,8203,56128,56430,8203,56128,56423,8203,56128,56447]),!b);case"emoji":return b=d([55357,56424,55356,57342,8205,55358,56605,8205,55357,56424,55356,57340],[55357,56424,55356,57342,8203,55358,56605,8203,55357,56424,55356,57340]),!b}return!1}function f(a){var c=b.createElement("script");c.src=a,c.defer=c.type="text/javascript",b.getElementsByTagName("head")[0].appendChild(c)}var g,h,i,j,k=b.createElement("canvas"),l=k.getContext&&k.getContext("2d");for(j=Array("flag","emoji"),c.supports={everything:!0,everythingExceptFlag:!0},i=0;i<j.length;i++)c.supports[j[i]]=e(j[i]),c.supports.everything=c.supports.everything&&c.supports[j[i]],"flag"!==j[i]&&(c.supports.everythingExceptFlag=c.supports.everythingExceptFlag&&c.supports[j[i]]);c.supports.everythingExceptFlag=c.supports.everythingExceptFlag&&!c.supports.flag,c.DOMReady=!1,c.readyCallback=function(){c.DOMReady=!0},c.supports.everything||(h=function(){c.readyCallback()},b.addEventListener?(b.addEventListener("DOMContentLoaded",h,!1),a.addEventListener("load",h,!1)):(a.attachEvent("onload",h),b.attachEvent("onreadystatechange",function(){"complete"===b.readyState&&c.readyCallback()})),g=c.source||{},g.concatemoji?f(g.concatemoji):g.wpemoji&&g.twemoji&&(f(g.twemoji),f(g.wpemoji)))}(window,document,window._wpemojiSettings);
		</script>
		<style type="text/css">
img.wp-smiley,
img.emoji {
	display: inline !important;
	border: none !important;
	box-shadow: none !important;
	height: 1em !important;
	width: 1em !important;
	margin: 0 .07em !important;
	vertical-align: -0.1em !important;
	background: none !important;
	padding: 0 !important;
}
</style>
	<link rel='stylesheet' id='wp-block-library-css'  href='https://librivox.org/wp-includes/css/dist/block-library/style.min.css?ver=5.2.3' type='text/css' media='all' />
<link rel='stylesheet' id='style-css'  href='https://librivox.org/wp-content/themes/librivox/style.css?ver=5.2.3' type='text/css' media='all' />
<script type='text/javascript' src='https://librivox.org/wp-includes/js/jquery/jquery.js?ver=1.12.4-wp'></script>
<script type='text/javascript' src='https://librivox.org/wp-includes/js/jquery/jquery-migrate.min.js?ver=1.4.1'></script>
<link rel='https://api.w.org/' href='https://librivox.org/wp-json/' />
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://librivox.org/xmlrpc.php?rsd" />
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://librivox.org/wp-includes/wlwmanifest.xml" /> 
<meta name="generator" content="WordPress 5.2.3" />
<link rel="canonical" href="https://librivox.org/pages/about-librivox/" />
<link rel='shortlink' href='https://librivox.org/?p=37' />
<link rel="alternate" type="application/json+oembed" href="https://librivox.org/wp-json/oembed/1.0/embed?url=https%3A%2F%2Flibrivox.org%2Fpages%2Fabout-librivox%2F" />
<link rel="alternate" type="text/xml+oembed" href="https://librivox.org/wp-json/oembed/1.0/embed?url=https%3A%2F%2Flibrivox.org%2Fpages%2Fabout-librivox%2F&#038;format=xml" />
	
	<script type="text/javascript">

		var _gaq = _gaq || [];
		_gaq.push(['_setAccount', 'UA-1429228-8']);
		_gaq.push(['_trackPageview']);
		
		(function() {
		var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
		ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
		var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
		})();

	</script>

</head>

<body class="page-template-default page page-id-37 page-child parent-pageid-31540 wp" >

    <ul class="assistive-text">
      <li><a href="#sub-menu">Skip to navigation</a></li>
      <li><a href="#main-content">Skip to front page content</a></li>
      <li><a href="#secondary-content">Skip to secondary content</a></li>
      <li><a href="#footer">Skip to footer</a></li>
    </ul>
  

<section class="header-wrap">
		<header class="site-header">
		
			<!-- Site title/Logo and tagline -->
			<hgroup class="logo-wrap">
								<h4 class="logo"><a href="https://librivox.org/" title="LibriVox" rel="home"><img src="https://librivox.org/wp-content/themes/librivox/images/librivox-logo.png" alt="librivox-logo" width="180" height="37"><span class="assistive-text">Librivox</span></a></h4>				
				<h3 class="tagline">free public domain audiobooks</h3>
			</hgroup>  
				
			<!-- Sub menu -->
			<nav class="sub-menu" id="sub-menu">
				<h1 class="assistive-text icon-fontawesome-webfont"><span>Menu</span></h1>
				<ul id="menu-top" class="sub-menu-list"><li id="menu-item-31535" class="menu-item menu-item-type-post_type menu-item-object-page current-menu-item page_item page-item-37 current_page_item menu-item-31535"><a href="https://librivox.org/pages/about-librivox/" aria-current="page">About</a></li>
<li id="menu-item-31637" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-31637"><a href="https://librivox.org/pages/contact-librivox/">Contact</a></li>
<li id="menu-item-31381" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-31381"><a href="http://forum.librivox.org">Forum</a></li>
<li id="menu-item-31638" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-31638"><a href="https://librivox.org/pages/help/">Help</a></li>
<li id="menu-item-8" class="twitter menu-item menu-item-type-custom menu-item-object-custom menu-item-8"><a href="http://twitter.com/librivox">Twitter</a></li>
<li id="menu-item-9" class="rss menu-item menu-item-type-custom menu-item-object-custom menu-item-9"><a href="/pages/librivox-feeds">Rss</a></li>
</ul>					
			</nav><!-- end sub-menu -->   

 
			<!-- Search Form -->
		<div class="search-wrap">		
			 <form action="https://librivox.org/search" role="search" id="searchform" method="get" class="searchform">
				 <label class="assistive-text" for="s">Search Librivox</label>
				 <input placeholder="Search by Author, Title or Reader" id="q" name="q" class="field" />
				 <input type="submit" value="Search" id="searchsubmit"  class="submit" />
			</form>	
			<a href="https://librivox.org/search/advanced_search" class="advanced-search"> Advanced search</a>	
		</div>	


		<script type="text/javascript">
			document.getElementById('searchsubmit').onclick=function(e)
			{
				e.preventDefault();
				var q = document.getElementById('q').value;
				window.location.href = "https://librivox.org/search/q/" + q;
			}
			
		</script>



  	 </header> <!-- end #header-->
      
</section> <!-- end #header-wrap--> 	 <section class="main-content">	
					
			<div  class="primary-content">		   
				 

			

								<div id="post-37"  class="post-wrap post-37 page type-page status-publish hentry">

					 		
					 		    	 
					 	 <h1 class="post-title">About LibriVox</h1>
					 	 
					 	   
			      
					  				
				      				  
				      <div class="post-content">  
					  	<h2>LibriVox Objective</h2>
<blockquote><p>To make all books in the public domain available, for free, in audio format on the internet.</p></blockquote>
<h2>Our Fundamental Principles</h2>
<ul>
<li>Librivox is a non-commercial, non-profit and ad-free project</li>
<li>Librivox donates its recordings to the public domain</li>
<li>Librivox is powered by volunteers</li>
<li>Librivox maintains a loose and open structure</li>
<li>Librivox welcomes all volunteers from across the globe, in all languages</li>
</ul>
<h3>More Information</h3>
<p><a href="#1">What We Do</a></p>
<p><a href="#2">Resources and Partners</a></p>
<p><a href="#3">In the Press</a></p>
<p><a href="#4">Inspirations</a></p>
<p><a href="#5">The Beginning</a></p>
<p><a href="#6">Contact</a></p>
<h3><a name="1"></a>What We Do</h3>
<p>LibriVox volunteers record chapters of books in the <a href="/pages/public-domain/">public domain</a>, and then we <a href="/pages/about-listening-to-librivox/">release the audio files</a> back onto the net for free. All our audio is in the public domain, so you may use it for whatever purpose you wish. <strong>Please note:</strong> Our readers are free to choose the books they wish to record. LibriVox sees itself as a library of audiobooks. Because the books we read are in the public domain, our readers and listeners should be aware that many of them are very old, and may contain language or express notions that are antiquated at best, offending at worst.</p>
<p><a href="/pages/volunteer-for-librivox/">Volunteering for LibriVox</a> is easy and does not require any experience with recording or audio engineering or acting or public speaking. All you need is a computer, a microphone, some free recording software, and your own voice. We accept all volunteers in all languages, with all kinds of accents. You&#8217;re welcome to volunteer to read any language you speak, as long as you can make yourself understood in it. You don&#8217;t need to audition, but we do suggest a <a href="http://wiki.librivox.org/index.php/1-Minute_Test">1-Minute Test</a> recording just to check your setup. We&#8217;ll accept you no matter what you sound like.</p>
<p>We operate almost exclusively through Internet communications on our <a href="http://librivox.org/forum">forum</a>, where all your questions will be answered by our friendly community.</p>
<p>For more detailed information, see our <a href="https://forum.librivox.org/viewtopic.php?p=1354#p1354">FAQ</a>.</p>
<p>We&#8217;d like your help. Click to learn about <a href="/pages/volunteer-for-librivox/">volunteering for LibriVox.</a></p>
<h3><a name="2"></a>Resources and Partners</h3>
<p>We get most of our texts from <a href="http://www.gutenberg.org">Project Gutenberg</a>, and the <a href="http://archive.org">Internet Archive</a> hosts our audio files (for free!).</p>
<p>In early 2010 we ran a fund-raising drive to raise $20,000 for our expenses for the next few years. In July 2013 we launched a new fund-raising drive with the goal of raising $50,000 for short and long term expenses. If you would like to help, please visit our <a href="/pages/how-to-donate/">Donate Page</a>.</p>
<h3><a name="3"></a>In the Press</h3>
<p>Some press articles about LibriVox have appeared in the following:</p>
<ul>
<li><a href="http://www.reason.com/news/show/119240.html">Reason Magazine</a></li>
<li><a href="http://librivox.org/2006/01/15/la-times-on-librivox/">Los Angeles Times</a></li>
<li><a href="http://librivox.org/2006/10/14/montreal-gazette-on-librivox/">Montreal Gazette</a></li>
<li><a href="http://www.nytimes.com/2006/08/25/books/25audi.html">New York Times</a></li>
<li><a href="http://www.redhat.com/magazine/017mar06/features/librivox/">red hat magazine</a></li>
<li><a href="http://librivox.org/2006/02/07/librivox-on-bbcs-the-world/">The World &#8211; BBC Radio</a></li>
<li><a href="http://www.wired.com/culture/lifestyle/news/2005/12/69780">wired.com</a></li>
<li><a href="http://www.itconversations.com/shows/detail1783.html">IT conversations (audio)</a></li>
<li><a href="http://creativecommons.org/text/librivox">creative commons</a></li>
<li><a href="http://en.wikinews.org/wiki/Interview_with_LibriVox_founder_Hugh_McGuire">wikinews</a></li>
<li><a href="http://www.lesechos.fr/info/innovation/300189432.htm">Les Echos (fr)</a></li>
</ul>
<h3><a name="4"></a>Inspirations</h3>
<p>LibriVox was inspired by <a href="http://akma.disseminary.org/archives/001253.html">AKMA’s audio volunteer project</a> that brought <a href="http://lessig.org">Lawrence Lessig’s</a> book, <a href="http://www.free-culture.cc/">Free Culture</a>, to your ears.</p>
<p>Other inspirations include:</p>
<ul>
<li><a href="http://urbanartadventures.com/">Urban Art Adventures’</a> and the podchef</li>
<li><a href="http://www.wikipedia.org">Wikipedia </a></li>
<li><a href="http://fsf.org/">Richard Stallman &amp; the Free Software movement</a></li>
<li><a href="http://gutenberg.org">Project Gutenberg</a></li>
<li><a href="http://www.creativecommons.org/">Creative Commons</a></li>
<li><a href="http://archive.org">Internet Archive</a></li>
<li>Brewster Kahle’s talk: <a href="http://www.itconversations.com/shows/detail400.html">Universal Access to All Human Knowledge</a></li>
</ul>
<h3><a name="5"></a>The Beginning</h3>
<p>LibriVox was started in August 2005, by <a href="http://hughmcguire.net">Hugh McGuire</a>. An interview with Paula B from <a href="http://www.writingshow.com/">The Writing Show</a> describing <a href="http://www.writingshow.com/podcasts/2005/08232005.html">LibriVox in its earliest days can be found here</a>.</p>
<h3><a name="6"></a>Contact</h3>
<ul>
<li>If you want to give feedback, please <a href="/pages/feedback/">read this first.</a></li>
<li>The best way to get in touch is on our <a href="http://librivox.org/forum">Forum</a>.</li>
<li>Send us an email at: <strong><strong><a href="mailto:info[AT]librivox.org">info[AT]librivox[DOT]org</a></strong></strong></li>
</ul>
					 </div>
				  
					 				  
				    
					  
			   </div><!-- end .post-wrap -->

					  	
			 
		     </div><!-- end .primary-content -->
		     
     
		   <div class="secondary-content">
		        	<h3>Browse the catalog </h3>
	<!-- Sidebar MAIN MENU -->
	<nav class="main-menu-list-wrap ">
		<ul id="menu-main" class="main-menu-list"><li id="menu-item-5" class="author-btn menu-item menu-item-type-custom menu-item-object-custom menu-item-5"><a title="Brows LibriVox Catalog by Author" href="http://librivox.org/search/author">Author</a></li>
<li id="menu-item-10" class="title-btn menu-item menu-item-type-custom menu-item-object-custom menu-item-10"><a title="Brows LibriVox Catalog by Author" href="http://librivox.org/search/title">Title</a></li>
<li id="menu-item-6" class="genre-btn menu-item menu-item-type-custom menu-item-object-custom menu-item-6"><a title="Brows LibriVox Catalog by Genre/Subject" href="http://librivox.org/search/genre">Genre/Subject</a></li>
<li id="menu-item-7" class="language-btn menu-item menu-item-type-custom menu-item-object-custom menu-item-7"><a title="Brows LibriVox Catalog by Language" href="http://librivox.org/search/language">Language</a></li>
</ul>	</nav>	
	<ul class="sidebar-widget-wrap">
		
						<li id="recent-posts-2" class="widget widget_recent_entries">		<h3 class="widget-title">Recent Posts</h3>		<ul>
											<li>
					<a href="https://librivox.org/2020/03/02/world-tour-2020-central-and-south-africa/">World Tour 2020: Central and South Africa</a>
									</li>
											<li>
					<a href="https://librivox.org/2020/02/01/world-tour-2020-south-and-central-america/">World Tour 2020: South and Central America</a>
									</li>
											<li>
					<a href="https://librivox.org/2020/01/01/world-tour-2020-australia-new-zealand-and-thereabouts/">World Tour 2020: Australia, New Zealand and thereabouts</a>
									</li>
											<li>
					<a href="https://librivox.org/2019/12/01/a-spiritual-time/">A Spiritual Time</a>
									</li>
											<li>
					<a href="https://librivox.org/2019/11/09/lurking-in-the-dark/">Lurking in the Dark&#8230;</a>
									</li>
					</ul>
		</li>	
	</ul>		   </div>
		   
     
 	 </section> <!-- end .main-content -->

	 

	<footer class="footer-wrap" id="footer">
			<div class="footer">
				<a class="license" href="#"><img src="https://librivox.org/wp-content/themes/librivox/images/public-domain-license.gif" alt="public-domain-license" width="88" height="31" /></a>

							<div class="textwidget"><strong>Librivox</strong> - Acoustical liberation of books in the public domain.

<p style="font-size: 0.9em;">(For users in the European Union or Switzerland, <a href="https://librivox.org/pages/translation-german-pages/">please read this note.</a>)</p></div>
		
			</div><!-- end .footer-wrap -->	
		</footer>
        <script type='text/javascript' src='https://librivox.org/wp-content/themes/librivox/js/small-menu.js?ver=v1'></script>
<script type='text/javascript' src='https://librivox.org/wp-includes/js/wp-embed.min.js?ver=5.2.3'></script>
  </body>
</html>
"""