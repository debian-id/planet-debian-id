/* Log to the console if we can: firebug firefox extension will view these */
function log( txt)
{
   if (  window.console && window.console.log )
   {
     window.console.log( txt );
   }
}

/* create a cookie */
function createCookie(name,value,days)
{
   var expires = "";
   if (days)
   {
      var date = new Date();
      date.setTime(date.getTime()+(days*24*60*60*1000));
      expires = "; expires="+date.toGMTString();
   }
   document.cookie = name+"="+value+expires+"; path=/";
   log( "Created cookie: " + document.cookie );
}

/* read a cookie */
function readCookie(name)
{
   var nameEQ = name + "=";
   var ca = document.cookie.split(';');
   for(var i=0;i < ca.length;i++)
   {
      var c = ca[i];
      while (c.charAt(0)==' ')
         c = c.substring(1,c.length);

      if (c.indexOf(nameEQ) == 0)
         return c.substring(nameEQ.length,c.length);
   }
   return null;
}

/* erase a cookie */
function eraseCookie(name)
{
    log( "erasingCookie" );
    createCookie(name,"",-1); 
}

/* exclude entries from the same domain as the given URL */
function exclude( site )
{
    log( "Excluding: " + site );

    domain = site.match( /:\/\/(\.*)([^/:]+)/ );
    domain = domain[2]?domain[2]:'';

    var val=readCookie('excludes');
    if ( !val )
    { 
	val = '';
    }
    if ( val.length > 0 )
    {
       val = val + ",";
    }
    val = val + domain
    createCookie('excludes',val, 10);
}

/* un-exclude host */
function show( site )
{
    domain = site.match( /:\/\/(\.*)([^/:]+)/ );
    domain = domain[2]?domain[2]:'';

    log( "Showing " + site );

    /* get the cookie */
    var val=readCookie('excludes');
    if ( !val ) { val = ''; }

    /* new cookie value */
    var n = '';

    hosts=val.split( ',' );
    for( var i=0 ; i < hosts.length; i++ )
    {
      /* the currently excluded host isn't the one we're to show now - so keep it */
      if ( hosts[i] != domain )
      {
          if ( n.length > 0 ) { n = n + ',' ; }
          n += hosts[i];
      }
      else
      {
         /* the currently excluded host is now supposed to be visible.. */
          c = getElementsByClassNamePrefix( hosts[i] );
          for ( var j = 0; j < c.length; j++ )
          {
              showDiv(c[j].id );
              showInlineDiv( ( c[j].id + "_hide" ) )
	      hideDiv( ( c[j].id + "_show" ) )
          }
      }
    }
    /* set new cookie */
    createCookie('excludes',n, 10);
}

/* avoid excluding any sites : clear the cookie */
function excludeNone()
{
    eraseCookie( 'excludes' );
    window.location.reload();
    hideDiv( 'unhide-all' );
}

/* hide the given div, if possible */
function hideDiv( id ) {
    i = document.getElementById(id);
    if ( i )
    {
	log( "Setting div " + id + " -> display:none;" );
        i.style.display="none";
    }
}

/* show the given div */
function showDiv( id ) {
    i = document.getElementById(id);
    if ( i )
    {
	log( "Setting div " + id + " -> display:block;" );
        i.style.display="block";
    }
}
function showInlineDiv( id ) {
    i = document.getElementById(id);
    if ( i )
    {
	log( "Setting div " + id + " -> display:inline;" );
        i.style.display="inline";
    }
}

/* get elements with a class starting with the given name */
function getElementsByClassNamePrefix(classname) {
         var els = document.getElementsByTagName("*");
         var c = new RegExp("/b^|" + classname  );
         final = new Array();
         var n=0;
         for (var i=0; i < els.length; i++) {
              if (els[i].className) {
                   if(c.test(els[i].className)) {
                   final[n] = els[i];
                   n++;
                   }
              }
         }
         return final;
}

/* hide all the hosts we're supposed to */
function hideHosts()
{
     var excl=readCookie( 'excludes');
     if ( ! excl ) { excl='' ; }
     hosts=excl.split( ',' );

     for ( var i = 0; i < hosts.length; i++ )
     {
          // ok so we have a host.  should we hide it?
          if ( hosts[i] )
          {
              c = getElementsByClassNamePrefix( hosts[i] );
              for ( var j = 0; j < c.length; j++ )
              {
                  hideDiv(c[j].id );
                  showInlineDiv( ( c[j].id + "_show" ) )
	          hideDiv( ( c[j].id + "_hide" ) )

		  showDiv( 'unhide-all' );
              }
          }
     }
}

