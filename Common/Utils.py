#!/usr/bin/env python
# -*- coding: utf-8 -*-


catalogBookRegex = r"<label class=\"itemlisting.*\" for=\"(.*)\">\\n<!-- title -->\\n<strong>(.*)<\/strong>\\n<!-- and\/or display linked 880 data -->\\n<!-- and\/or display linked 880 data -->\\n<!-- author -->\\n<br\/>(.*)<!-- and\/or display linked 880 data -->\\n<\/label>"

regex =  r"<td class=\"itemlisting.*?\">\s+<input type=\"checkbox\" name=\".*?\" id=\"RENEW.*?\">\s+<\/td>\s+<td class=\"itemlisting.*?\">\s+<label for=\"RENEW.*?\">\s+<!-- Print the title, if it exists -->\s+(.*?)\s+<!-- Print the author, if it exists -->\s+(.*?)\s+<\/label>\s+<\/td>\s+<td class=\"itemlisting.*?\">\s+devolución:\s+<!.. Print the date due -->\s+<strong>(.*?)<\/strong><br>"
testPage = '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<!-- Copyright (c) 2000 - 2008, SirsiDynix - Defines the head  body of each page. -->

<!-- entorno: GENERIC, número de la política de ENVN de la estación: 2 -->
<!-- Versión del servidor: 3.4.1.3.GA -->

<html lang="es" dir="ltr">

<head>

  <title>iLink Universidad de Alicante</title>


<!-- Set the expiration date to the past so the page will always be reloaded -->
  <meta http-equiv="Expires" content="Sun, 1 Jan 1995 08:00:00 CST">

  <!-- Not the login page -->

<!--  Copyright (c) 1997 - 2008, SirsiDynix - JavaScript functions defined in every page. -->
<script language="JavaScript" type="text/javascript">

// used by dynamic table sorting
var currentCol = 0;

function open_win(url) {
	new_win = window.open(url,"new_win",'toolbar=1,location=1,directories=0,status=1,menubar=1,scrollbars=1,resizable=1,width=750,height=250');
	if (new_win)
	{
	  new_win.focus();
	}
}

function open_bare_win(url) {
	new_b_win = window.open(url,"new_b_win",'toolbar=0,location=0,directories=0,status=1,menubar=0,scrollbars=1,resizable=1,width=620,height=450');
	if (new_win)
	{
	  new_b_win.focus();
	}
}

function open_hyperion_image_win(url) {
	hyperion_image_win = window.open(url,"hyperion_image_win",'toolbar=0,location=0,directories=0,status=1,menubar=0,scrollbars=1,resizable=1,width=600,height=450,screenX=410,screenY=210');
}

function open_hyperion_info_win(url) {
	hyperion_info_win = window.open(url,"hyperion_info_win",'toolbar=0,location=0,directories=0,status=1,menubar=0,scrollbars=1,resizable=1,width=400,height=450,screenX=0,screenY=210');
}

function open_win_timeout(url,timeout) {
	new_win = window.open(url,"new_win",'toolbar=0,location=0,directories=0,status=1,menubar=1,scrollbars=1,resizable=1,width=750,height=250');
	setTimeout("new_win.close()",timeout);
}

function open_help_win(url) {
  new_win = window.open(url,"help_win",'toolbar=0,location=0,directories=0,status=1,menubar=0,scrollbars=1,resizable=1,width=640,height=480');
  if (new_win)
  {
    new_win.focus();
  }
}

function open_bounce_win(url) {
  new_win = window.open(url,"bounce_win",'toolbar=0,location=0,directories=0,status=1,menubar=0,scrollbars=1,resizable=1,width=620,height=450');
}

/* Function for icon-type search form action */
function orig_form_action()
{
	if (!document.searchform.search_type[0].checked)
	  {
	  return true;
	  }
	else
	  {
          document.url_form.url.value = "http://www.google.com/search?q=" + document.searchform.searchdata1.value + "&safe=vss&vss=1&sa=Google+Search";
          open_win(document.url_form.url.value);
	  return false;
	  }
}

function combine_fields()
{
    document.getElementById("searchdata3").value="{LEXILE}>" + document.getElementById("lexilemin").value + "<" + document.getElementById("lexilemax").value;
    //alert (document.getElementById("searchdata3").value);
}

/* Function for icon-type search form action */
function search_form_action()
{
	var search_engine_checked = 0;
	var temp_str;

	for (var i = 0; i < document.searchform.search_type.length; i++)
	  {
	  if (document.searchform.search_type[i].value == "searchengine")
	    if (document.searchform.search_type[i].checked)
	      search_engine_checked = 1;
	  }

	if (!search_engine_checked)
	  {
	  return true;
	  }
	else
	  {
          temp_str = document.searchform.searchdata1.value;
	  temp_str = temp_str.replace(/\s+/g,"+");
          document.url_form.url.value = "http://www.google.com/search?q=" + temp_str + "&safe=vss&vss=1&sa=Google+Search";
          open_win(document.url_form.url.value);
	  return false;
	  }
}

function getNonJavaHelpFileUrl(langDir, file)
{
  if (file == "ibistro_overview") {
    return '/iBistro_helps/User/' + langDir + '/index.htm';
  }
  else {
    return '/iBistro_helps/User/' + langDir + '/index.htm?context=elibrary&topic=' + file;
  }
}


function put_help_button(langDir, alttextHelp, file)
{
  document.writeln('<a href="#" onclick="javascript:open_help_win(\''+getNonJavaHelpFileUrl(langDir,file)+'\')" alt="'+alttextHelp+'" title="'+alttextHelp+'">'+'<img src="/WebCat_Images/Castellano/Buttons/Link/HELP.gif" border="0" alt="AYUDA"  title="AYUDA">'+'<\/a>');
}


function put_keepremove_button(ckey,value)
{
  document.writeln('<img name="ickey-' + ckey + '"');
  document.writeln('src="/WebCat_Images/Castellano/Other/Miscil/clear.gif"');
  document.writeln('alt="' + value + '" border="0">');

  document.writeln('<input type="button"');
  if (value == 'Guardar')
    {
    document.writeln('class="itemdetails"');
    }
  else
    {
    document.writeln('class="itemdetails2"');
    }
  document.writeln('name="ckey-' + ckey + '"');
  document.writeln('id="ckey-' + ckey + '"');
  document.writeln('value="' + value + '" alt="' + value + '"');
  document.writeln('onClick="javascript:updatekeptlist(this,' + ckey + ');">');
}

function updatekeptlist(myButton,ckey)
{
  key = "i" + myButton.name;
  if (myButton.value == 'Guardar')
    {
    myImage = new Image();
    myImage.src = '/uhtbin/cgisirsi/?ps=lVBEUv4VBl/0/235110023/125/ADD?kept-' + ckey + '=on';
    document.images[key].src=myImage.src;
    myImage = new Image();
    myImage.src = '/WebCat_Images/Castellano/Other/Miscil/clear.gif';
    document.images[key].src=myImage.src;
    document.images[key].alt='Suprimir';
    myButton.value='Suprimir';
		myButton.className='itemdetails2';
    }
  else
    {
    myImage = new Image();
    myImage.src = '/uhtbin/cgisirsi/?ps=26ktz3qj2H/0/235110023/125/REMOVE?kept-' + ckey + '=on';
    document.images[key].src=myImage.src;
    myImage = new Image();
    myImage.src = '/WebCat_Images/Castellano/Other/Miscil/clear.gif';
    document.images[key].src=myImage.src;
    document.images[key].alt='Guardar';
    myButton.value='Guardar';
		myButton.className='itemdetails';
  }
}


function put_keepremove_all_button()
{
  document.writeln('<img name="ckey-ALL"');
  document.writeln('src="/WebCat_Images/Castellano/Other/Miscil/clear.gif"');
  document.writeln('alt="' + 'Guardar página' + '" border="0">');

  document.writeln('<input type="button"');
  document.writeln('class="itemdetails"');
  document.writeln('style="width: 145;"');
  document.writeln('name="ckey-ALL"');
  document.writeln('value="' + 'Guardar página' + '" alt="' + 'Guardar página' + '"');
  document.writeln('onClick="javascript:updatekeptlist_all(this,keep_ckeys_array);">');
}

function updatekeptlist_all(myButton,ckeys_array)
{
  var ckey_str = new String("");

  for (i=0; i<ckeys_array.length; i++)
  {
    ckey_str = ckey_str + "kept-" + ckeys_array[i] + "=on&";
  }
  key = myButton.name;
  myImage = new Image();
  myImage.src = '/uhtbin/cgisirsi/?ps=gT7KlN7eNg/0/235110023/125/ADD?' + ckey_str;
  document.images[key].src=myImage.src;

  // Change all individual Keep buttons to "marked"
  for (i=0; i<ckeys_array.length; i++)
  {
    ckey = ckeys_array[i];
    element_id = "ckey-" + ckey;
    document.images["i" + element_id].alt='Suprimir';
    document.getElementById(element_id).value='Suprimir';
    document.getElementById(element_id).className='itemdetails2';
  }
  myImage = new Image();
  myImage.src = '/WebCat_Images/Castellano/Other/Miscil/clear.gif';
  document.images[key].src=myImage.src;
}

function do_history(form)
  {
  // Based on the value of the srch_history <select> list, set the search input fields.
  var opt_idx;
  var i = 0;
  opt_idx = form.srch_history.selectedIndex;
  // The history "value" is formatted:  "term^label^library"
  valueArray = form.srch_history.options[opt_idx].value.split("^");
  // Set the search term
  form.searchdata1.value = valueArray[0];
  // Set the search type - if it is present
  if (form.srchfield1 != null)
    {
    for (i<0; i<form.srchfield1.length; i++)
      {
      if (form.srchfield1.options[i].text == valueArray[1])
        {
        form.srchfield1.options[i].selected = true;
        break;
        }
      }
    }
  // Set the library
  form.library.value = valueArray[2];
  }



function sendOpenURL(inISBN,inTITLE,inISSN,inGENRE)
{
	aWindow = window.open('','','toolbar=1,location=1,directories=0,status=1,menubar=1,scrollbars=1,resizable=1,width=750,height=250');
	
	if (aWindow.document.body == null)
	  {
	  aBody = aWindow.document.createElement('body');
	  aWindow.document.appendChild(aBody);
	  }

        nFORM=aWindow.document.createElement('form');
	nFORM.action='';
	nFORM.target="_self";
	nFORM.method="post";
	nFORM.name="OpenURL";

	if (inISBN.length != 0)
	  {
	  nISBN=aWindow.document.createElement('input');
	  nISBN.name='isbn';
	  nISBN.value=inISBN;
	  nISBN.type='hidden';

	  nFORM.appendChild(nISBN);
	  }

	if (inTITLE.length != 0)
	  {
	  nTITLE=aWindow.document.createElement('input');
	  nTITLE.name='title';
	  nTITLE.value=inTITLE;
	  nTITLE.type='hidden';

	  nFORM.appendChild(nTITLE);
	  } 

	if (inISSN.length != 0)
	  {
	  nISSN=aWindow.document.createElement('input');
	  nISSN.name='issn';
	  nISSN.value=inISSN;
	  nISSN.type='hidden';

	  nFORM.appendChild(nISSN);
	  }

	if (inGENRE.length != 0)
	  {
	  nGENRE=aWindow.document.createElement('input');
	  nGENRE.name='genre';
	  nGENRE.value=inGENRE;
	  nGENRE.type='hidden';

	  nFORM.appendChild(nGENRE);
	  }

	aWindow.document.body.appendChild(nFORM);

	nFORM.submit();

	aWindow.document.body.removeChild(nFORM);

}

function sendEnvisionWare(inUser,inPassword)
{
	aWindow = window.open('','','toolbar=1,location=1,directories=0,status=1,menubar=1,scrollbars=1,resizable=1,width=750,height=250');
	
	if (aWindow.document.body == null)
	  {
	  aBody = aWindow.document.createElement('body');
	  aWindow.document.appendChild(aBody);
	  }

	if (0 == 1)
	  strPassword = '';
	else
          strPassword = inPassword;

        nFORM=aWindow.document.createElement('form');
	nFORM.action='';
	nFORM.target="_self";
	nFORM.method="post";
	nFORM.name="EnvisionWare";
	
	nuid=aWindow.document.createElement('input');
	nuid.id='user_id';
	nuid.name='user_id';
	nuid.value=inUser;
	nuid.type='hidden';

	nFORM.appendChild(nuid);

	npassword=aWindow.document.createElement('input');
	npassword.id='password';
	npassword.name='password';
	npassword.value=strPassword;
	npassword.type='hidden';

	nFORM.appendChild(npassword);

	aWindow.document.body.appendChild(nFORM);

	nFORM.submit();

	aWindow.document.body.removeChild(nFORM);
}

function sendAxis(inUser,inLibrary,inBill,inTotal,inAmount)
{

	currencyStr = 'E';

	if (currencyStr == "$")
	  {
	  currencyStr = "\\" + currencyStr;  
	  }

	re = new RegExp(currencyStr,"g");

	inTotal = inTotal.replace(re,"");

	inAmount = inAmount.replace(re,"");

	strTotal = inTotal;
	strAmount = inAmount;

	strTotal = strTotal.replace(".","");
	strAmount = strAmount.replace(".","");

	strRef = inUser + '|' + inLibrary + '|';
	strRef = strRef + inBill + '|' + strTotal + '|';
	strRef = strRef + strAmount;

	// convert the strings to numbers and 
        // test for minimum before opening window
	
	if (inAmount.indexOf(",") == -1)
	  {
	  floatAmount = parseFloat(inAmount);
	  }
	else
	  {
	    floatAmount = 0.0;
	    workstr = inAmount;
	    while (workstr.indexOf(",") != -1)
	      {
		partialstr = workstr.substr(0,workstr.indexOf(","));
		floatAmount = floatAmount + parseFloat(partialstr);
		workstr = workstr.substr(workstr.indexOf(",") + 1);
	      }
	    floatAmount = floatAmount + parseFloat(workstr);
	  }

	floatAmount = Math.round(floatAmount*100)/100;

	aWindow = window.open('','','toolbar=1,location=1,directories=0,status=1,menubar=1,scrollbars=1,resizable=1,width=750,height=250');
	
	if (aWindow.document.body == null)
	  {
	  aBody = aWindow.document.createElement('body');
	  aWindow.document.appendChild(aBody);
	  }

        nFORM=aWindow.document.createElement('form');
	nFORM.action='';
	nFORM.target="_self";
	nFORM.method="post";
	nFORM.name="AXIS";

	nRequid=aWindow.document.createElement('input');
	nRequid.name='requid';
	nRequid.value=strRef;
	nRequid.type='hidden';

	nFORM.appendChild(nRequid);
	
	nAmount=aWindow.document.createElement('input');
	nAmount.name='amt';
	nAmount.value=floatAmount;
	nAmount.type='hidden';

	while((nAmount.value.length - nAmount.value.indexOf(".")) < 3)
	  {
          nAmount.value = nAmount.value + "0";
	  }

	nFORM.appendChild(nAmount);
	
	nReturnURL=aWindow.document.createElement('input');
	nReturnURL.name='rurl';
	nReturnURL.value='';
	nReturnURL.type='hidden';

	nFORM.appendChild(nReturnURL);
	
	nBackURL=aWindow.document.createElement('input');
	nBackURL.name='back.url';
	nBackURL.value='';
	nBackURL.type='hidden';

	nFORM.appendChild(nBackURL);

	nSource=aWindow.document.createElement('input');
	nSource.name='source';
	nSource.value='I';
	nSource.type='hidden';

	nFORM.appendChild(nSource);
	
	nFundCode=aWindow.document.createElement('input');
	nFundCode.name='fund.code';
	nFundCode.value='';
	nFundCode.type='hidden';

	nFORM.appendChild(nFundCode);
	
	nFundName=aWindow.document.createElement('input');
	nFundName.name='fund.name';
	nFundName.value='';
	nFundName.type='hidden';

	nFORM.appendChild(nFundName);
	
	nRefNumber=aWindow.document.createElement('input');
	nRefNumber.name='ref';
	nRefNumber.value='';
	nRefNumber.type='hidden';

	nFORM.appendChild(nRefNumber);
	
	nRefNumberTwo=aWindow.document.createElement('input');
	nRefNumberTwo.name='ref2';
	nRefNumberTwo.value='';
	nRefNumberTwo.type='hidden';

	nFORM.appendChild(nRefNumberTwo);
	
	aWindow.document.body.appendChild(nFORM);

	nFORM.submit();

	aWindow.document.body.removeChild(nFORM);
}

function sendPayPal(inUser,inLibrary,inBill,inTotal,inAmount,inBillUser)
{

	currencyStr = 'E';

	if (currencyStr == "$")
	  {
	  currencyStr = "\\" + currencyStr;  
	  }

	re = new RegExp(currencyStr,"g");

	inTotal = inTotal.replace(re,"");

	inAmount = inAmount.replace(re,"");

	// convert the strings to numbers and 
        // test for minimum before opening window
	
	if (inAmount.indexOf(",") == -1)
	  {
	  floatAmount = parseFloat(inAmount);
	  }
	else
	  {
	    floatAmount = 0.0;
	    workstr = inAmount;
	    while (workstr.indexOf(",") != -1)
	      {
		partialstr = workstr.substr(0,workstr.indexOf(","));
		floatAmount = floatAmount + parseFloat(partialstr);
		workstr = workstr.substr(workstr.indexOf(",") + 1);
	      }
	    floatAmount = floatAmount + parseFloat(workstr);
	  }

	floatAmount = Math.round(floatAmount*100)/100;

	floatMinimum = parseFloat(0);

	if (floatAmount < floatMinimum)
	  {
	    alert ("La cantidad adeudada es menor que el mínimo para utilizar PayPal");
	    return;
	  }	  
	
	aWindow = window.open('','','toolbar=1,location=1,directories=0,status=1,menubar=1,scrollbars=1,resizable=1,width=750,height=250');
	
	if (aWindow.document.body == null)
	  {
	  aBody = aWindow.document.createElement('body');
	  aWindow.document.appendChild(aBody);
	  }


        nFORM=aWindow.document.createElement('form');
	nFORM.action='';
	nFORM.target="_self";
	nFORM.method="post";
	nFORM.name="PayPal";

	nCustom=aWindow.document.createElement('input');
	nCustom.name='custom';
	nCustom.value='user=' + inUser + '&';
	nCustom.value=nCustom.value + 'library=' + inLibrary + '&';
	nCustom.value=nCustom.value + 'bill_number=' + inBill + '&';
	nCustom.value=nCustom.value + 'total_owed=' + inTotal + '&';
	nCustom.value=nCustom.value + 'amount_paid=' + inAmount + '&';
	nCustom.value=nCustom.value + 'bill_user_id=' + inBillUser;
	nCustom.type='hidden';

	nFORM.appendChild(nCustom);

	nAmount=aWindow.document.createElement('input');
	nAmount.name='amount';
	nAmount.value=floatAmount;
	nAmount.type='hidden';

	nFORM.appendChild(nAmount);
	
	nCmd=aWindow.document.createElement('input');
	nCmd.name='cmd';
	nCmd.value='_xclick';
	nCmd.type='hidden';

	nFORM.appendChild(nCmd);
	
	nBusiness=aWindow.document.createElement('input');
	nBusiness.name='business';
	nBusiness.value='';
	nBusiness.type='hidden';

	nFORM.appendChild(nBusiness);
	
	nItemName=aWindow.document.createElement('input');
	nItemName.name='item_name';
	nItemName.value='bill payment';
	nItemName.type='hidden';

	nFORM.appendChild(nItemName);
	
	nNotifyURL=aWindow.document.createElement('input');
	nNotifyURL.name='notify_url';
	nNotifyURL.value='';
	nNotifyURL.type='hidden';

	nFORM.appendChild(nNotifyURL);
	
	nCurrencyCode=aWindow.document.createElement('input');
	nCurrencyCode.name='currency_code';
	nCurrencyCode.value='USD';
	nCurrencyCode.type='hidden';

	nFORM.appendChild(nCurrencyCode);

	aWindow.document.body.appendChild(nFORM);

	nFORM.submit();

	aWindow.document.body.removeChild(nFORM);
}

function clearCreditCardFields()
{
	ouracct_number=document.getElementById("acct_number");
	ouracct_name=document.getElementById("acct_name");
	ourexp_date=document.getElementById("exp_date");
	ouracct_number.value="";
	ouracct_name.value="";
	ourexp_date.value="";
}

function submitVeriSign(inUser,inData)
{
	nFORM=document.createElement('form');
	document.body.appendChild(nFORM);
	nFORM.action='/uhtbin/cgisirsi/?ps=GqvgRkyWiR/0/235110023/144';
	nFORM.target="_self";
	nFORM.method="post";
	nFORM.name="Payment";
	
	nUser=document.createElement('input');
	nUser.name='user_id';
	nUser.value=inUser;
	nUser.type='hidden';

	nFORM.appendChild(nUser);

	nData=document.createElement('input');
	nData.name='data';
	nData.value=inData;
	nData.type='hidden';

	nFORM.appendChild(nData);

	nFORM.submit();
}

function OpenGateway(inURL,inGateway)
{
	var need_to_replace = 0;

	
	  need_to_replace = 1;
	
	if (need_to_replace)
	  {
	  inURL = inURL.replace(":///","://"+location.host+"/");
	  }

	aWindow = window.open('','','toolbar=0,location=0,directories=0,status=1,menubar=0,scrollbars=1,resizable=1,width=600,height=600');

	inUserId = '018059602';
	inPassword = '3218';

	if (aWindow.document.body == null)
	  {
	  aBody = aWindow.document.createElement('body');
	  aWindow.document.appendChild(aBody);
	  }

        nFORM=aWindow.document.createElement('form');
	nFORM.action=inURL;
	nFORM.target="_self";
	nFORM.method="post";
	nFORM.name="Gateway";

	if (inGateway.length != 0)
	  {
	  nGateway=aWindow.document.createElement('input');
	  nGateway.name='new_gateway_db';
	  nGateway.value=inGateway;
	  nGateway.type='hidden';

	  nFORM.appendChild(nGateway);
	  }

	if (inUserId.length != 0)
	  {
	  nUser=aWindow.document.createElement('input');
	  nUser.name='user_id';
	  nUser.value=inUserId;
	  nUser.type='hidden';

	  nFORM.appendChild(nUser);
	  } 

	if (inPassword.length != 0)
	  {
	  nPIN=aWindow.document.createElement('input');
	  nPIN.name='password';
	  nPIN.value=inPassword;
	  nPIN.type='hidden';

	  nFORM.appendChild(nPIN);
	  }

	aWindow.document.body.appendChild(nFORM);

	nFORM.submit();

	aWindow.document.body.removeChild(nFORM);

}

function stripLeading(inString)
{
	while (inString.indexOf(" ") == 0 || inString.indexOf("\n") == 0 || inString.indexOf("\t") == 0)
	  {
	  inString = inString.substr(1);
	  }

	return inString;
}

function removeExtra(inString)
{
	 inString = inString.replace(/<(.|\n)+?>/g,"");
	 inString = inString.replace(/ /g,"");
	 inString = inString.replace(/\n/g,"");

	 return inString;
}

function pullAmount(inString)
{
	var reMoney;
	var result;
	var strWork;
	var portion;

	reMoney = new RegExp("^\\E\\d+(\\.\\d\\d)?$");
	result = reMoney.exec(inString);
	if (!reMoney.test(inString))
	  {
	  result = "$0.00,";
	  }
	strWork = new String(result);
	strWork = strWork.replace(/\E/g,"");
	portion = strWork.split(",");
	inString = portion[0];

	return inString;
}

function CompareAlpha(a, b)
{
	var strA = a[currentCol].toLowerCase();
	var strB = b[currentCol].toLowerCase();
	var pieces;
	var i;
	var reDontConsider;
	// remove html wrappers to sort the title
	strA = strA.replace(/<(.|\n)+?>/g,"");
	strB = strB.replace(/<(.|\n)+?>/g,"");
	// remove items we don't want the sort to consider
	var strDontConsider = '\\bthe\\b,\\ba\\b,\\ban\\b,\\",\\t,\\n';
	pieces = strDontConsider.split(",");
	for (i = 0; i < pieces.length; i++)
	  {
	  reDontConsider = new RegExp(pieces[i],"g");
	  strA = strA.replace(reDontConsider,"");
	  strB = strB.replace(reDontConsider,""); 
	  }
	strA = stripLeading(strA);
	strB = stripLeading(strB);
	if (strA < strB) { return -1; }
	else
	  {
	  if (strA > strB) { return 1; }
	  else { return 0; }
	  }
}

function CompareDate(a, b)
{
	var pattern;
	var pieces;
	var result;
	var workdate;
	var portion;
	var datetype;
	var dateone;
	var datetwo;
	var workstring;

	datetype = 1; 

	switch(datetype)
	  {
	  case 0:
	      // American style dates MM/DD/YYYY
	      pattern = new RegExp("([1-9]|0[1-9]|1[012])[/]([1-9]|0[1-9]|[12][0-9]|3[01])[/](19|20)\\d\\d");
	      result = pattern.exec(a[currentCol]);
	      if (!pattern.test(a[currentCol]))
	        result = "01/01/2035";
	      workdate = new String(result);
	      portion = workdate.split(",");
	      dateone = new Date(portion[0]);
	      result = pattern.exec(b[currentCol]);
	      if (!pattern.test(b[currentCol]))
	        result = "01/01/2035";
	      workdate = new String(result);
	      portion = workdate.split(",");
	      datetwo = new Date(portion[0]);
	      break;
	  case 1:
	      // European style date DD/MM/YYYY
	      pattern = new RegExp("([1-9]|0[1-9]|[12][0-9]|3[01])[/]([1-9]|0[1-9]|1[012])[/](19|20)\\d\\d");
	      result = pattern.exec(a[currentCol]);
	      if (!pattern.test(a[currentCol]))
	        result = "01/01/2035";
	      workdate = new String(result);
	      portion = workdate.split(",");
	      workstring = new String(portion);
	      pieces = workstring.split("/");
	      dateone = new Date();
	      dateone.setDate(parseInt(pieces[0]));
	      dateone.setMonth(parseInt(pieces[1]) - 1);
	      dateone.setFullYear(parseInt(pieces[2]));
	      result = pattern.exec(b[currentCol]);
	      if (!pattern.test(b[currentCol]))
	        result = "01/01/2035";
	      workdate = new String(result);
	      portion = workdate.split(",");
	      workstring = new String(portion);
	      pieces = workstring.split("/");
	      datetwo = new Date();
	      datetwo.setDate(parseInt(pieces[0]));
	      datetwo.setMonth(parseInt(pieces[1]) - 1);
	      datetwo.setFullYear(parseInt(pieces[2]));
	      break;
	  case 2:
	      // Asian style dates YYYY/MM/DD
	      pattern = new RegExp("(19|20)\\d\\d[/]([1-9]|0[1-9]|1[012])[/](0[1-9]|[12][0-9]|3[01]|[1-9])");
	      result = pattern.exec(a[currentCol]);
	      if (!pattern.test(a[currentCol]))
		result = "2035/01/01,";
	      workdate = new String(result);
	      portion = workdate.split(",");
	      workstring = new String(portion);
	      pieces = workstring.split("/");
	      dateone = new Date();
	      dateone.setDate(parseInt(pieces[2]));
	      dateone.setMonth(parseInt(pieces[1]) - 1);
	      dateone.setFullYear(parseInt(pieces[0]));
	      result = pattern.exec(b[currentCol]);
	      if (!pattern.test(b[currentCol]))
		result = "2035/01/01,";
	      workdate = new String(result);
	      portion = workdate.split(",");
	      workstring = new String(portion);
	      pieces = workstring.split("/");
	      datetwo = new Date();
	      datetwo.setDate(parseInt(pieces[2]));
	      datetwo.setMonth(parseInt(pieces[1]) - 1);
	      datetwo.setFullYear(parseInt(pieces[0]));
	      break;
	  default:
	      dateone = new Date();
	      datetwo = new Date();
	      break;
	  }

	if (dateone < datetwo) { return -1; }
	else
	  {
	  if (dateone > datetwo) { return 1; }
	  else { return 0; }
	  }
}

function CompareNumeric(a, b)
{
	var numA = a[currentCol];
	var numB = b[currentCol];

	numA = stripLeading(numA);
	numA = removeExtra(numA);
	numA = parseInt(numA);
	if (isNaN(numA))
	  numA = 0;

	numB = stripLeading(numB);
	numB = removeExtra(numB);
	numB = parseInt(numB);
	if (isNaN(numB))
	  numB = 0;

        return numA - numB; 
}

function CompareMoney(a, b)
{
	var numA = a[currentCol];
	var numB = b[currentCol];

	numA = stripLeading(numA);
	numA = removeExtra(numA);
	numB = stripLeading(numB);
	numB = removeExtra(numB);
	numA = pullAmount(numA);
	numB = pullAmount(numB);

	numA = parseFloat(numA);
	numB = parseFloat(numB);

	numA = numA * 100;
	numB = numB * 100;

	numA = Math.round(numA);
	numB = Math.round(numB);

	if (isNaN(numA)) { return 0;}
	else
	  {
	  if (isNaN(numB)) { return 0; }
	  else { return numA - numB; }
	  }
}
function TableSort(myTable, myCallingObject, myType)
{
	// this function will determine the column number for
	// rectangular tables that have one column header
	// for each column.
	var aColumn = myCallingObject.cellIndex;
	TableSortByColumn(myTable, aColumn, myType, myCallingObject, 1);
}

function switchImage(myCallingObject)
{
	var aColumn = myCallingObject;
	var aPath = '/WebCat_Images/Castellano/Special/Link';
	var reImage;
	var result;
	
	var strTemp;

	strTemp = myCallingObject.innerHTML;

	// check if arrow is up or down
	reImage = new RegExp("DOWN.gif\">");
	if (!reImage.test(strTemp))
	  result = 1;
	else
	  result = 0;

	// remove the current image string
	strTemp = strTemp.replace(/<img src(.|\n)+?>/gi,"");

	if (result == 0)
	  {
	  strTemp = "<img src=\"" + aPath + "/UP.gif\"> " + strTemp;
	  }
	else
	  {
	  strTemp = "<img src=\"" + aPath + "/DOWN.gif\"> " + strTemp;
	  }

	myCallingObject.innerHTML = strTemp;
}

function setImageDown(myCallingObject, myStepBack)
{
	var aColumn = myCallingObject;
	var aPath = '/WebCat_Images/Castellano/Special/Link';
	var aRow;
	var aTableSection;
	var myCells;
	var myChildren;
	var myCount;
	var myCountToo;

	var strTemp;
	var strWork;
	
	strTemp = myCallingObject.innerHTML;

	if (myStepBack == 1)
	  {
	  // remove images from all columns
	  aRow = myCallingObject.parentNode;
	  myCells = aRow.childNodes;
	  for (myCount = 0; myCount < myCells.length; myCount++)
	    {
	    if (strTemp != myCells[myCount].innerHTML)
	      {
	      strWork = myCells[myCount].innerHTML;
	      if (strWork != null)
	        {
	        strWork = strWork.replace(/<img src(.|\n)+?>/gi,"");
	        myCells[myCount].innerHTML = strWork;
		}
	      }
	    }
	  }
	else
	  {
	  // have to get all rows in the multiple level column headers
	  aTableSection = myCallingObject.parentNode.parentNode;
	  myCells = aTableSection.childNodes;
	  for (myCount = 0; myCount < myCells.length; myCount++)
	    {
	    if (myCells[myCount] != null)
	      {
	      if (myCells[myCount].nodeType == 1)
	        {
		myChildren = myCells[myCount].childNodes;
		for (myCountToo = 0; myCountToo < myChildren.length; myCountToo++)
		  {
		  if (myChildren[myCountToo] != null && 
		      myChildren[myCountToo].nodeType == 1)
		    {
	            if (strTemp != myChildren[myCountToo].innerHTML)
	              {
	              strWork = myChildren[myCountToo].innerHTML;
	              if (strWork != null)
	                {
	                strWork = strWork.replace(/<img src(.|\n)+?>/gi,"");
	                myChildren[myCountToo].innerHTML = strWork;
		        }
	              }
		    }
	          }
	        }
	      }
	    }
	  }

	strTemp = myCallingObject.innerHTML;
	strTemp = strTemp.replace(/<img src(.|\n)+?>/gi,"");

	strTemp = "<img src=\"" + aPath + "/DOWN.gif\"> " + strTemp;

	myCallingObject.innerHTML = strTemp;

}

function check_for_sorted(myCallingObject)
{
	// If the column has an arrow then it is sorted
	var reImage;
	var result;
	var strTemp;

	strTemp = myCallingObject.innerHTML;

	// check if arrow is up or down
	reImage = new RegExp("<img src(.|\n)+?>","i");
	if (reImage.test(strTemp))
	  result = true;
	else
	  result = false;

	return result;
}

function TableSortByColumn(myTable, myColumn, myType, myCallingObject, myStepBack)
{
	var mySource = document.getElementById(myTable);
	var myRows = mySource.rows.length;
	var myCols = mySource.rows[0].cells.length;
	var i;
	var j;
	currentCol = myColumn;
	var myArray = new Array(myRows);
	for (i=0; i < myRows; i++)
	  {
	   myArray[i] = new Array(myCols);
	   for (j=0; j < myCols; j++)
	     {
	     if (mySource.rows[i].cells[j] != null)
	       myArray[i][j] = mySource.rows[i].cells[j].innerHTML;
	     else
	       myArray[i][j] = "";
	     }
	  }

	if (check_for_sorted(myCallingObject))
	  {
	  switchImage(myCallingObject);
	  myArray.reverse();
	  }
	else
	  {
	  setImageDown(myCallingObject,myStepBack);
	  switch (myType)
	    {
	    case "a":
	        myArray.sort(CompareAlpha);
	        break;
	    case "d":
	        myArray.sort(CompareDate);
	        break;
	    case "n":
	        myArray.sort(CompareNumeric);
	        break;
	    case "m":
	        myArray.sort(CompareMoney);
	        break;
	    default:
		myArray.sort(CompareAlpha);
		break;
	    }
	  }

	for (i=0; i < myRows; i++)
	  {
	  for (j=0; j < myCols; j++)
	    {
            if (mySource.rows[i].cells[j] != null)
	      mySource.rows[i].cells[j].innerHTML = myArray[i][j];
	    }
	  }
}

function OnlineUserRegistrationCheck(formobj){
	// Enter name of mandatory fields
	var fieldRequired = Array("firstname", "lastname", "street", "city", "state", "zip", "pin", "validatepin");
	// Enter field description to appear in the dialog box
	var fieldDescription = Array("First Name", "Last Name", "Street", "City", "State", "Zip", "PIN", "Re-Type PIN");
	// dialog message
	var alertMsg = "" + ":\n";

	var l_Msg = alertMsg.length;

	for (var i = 0; i < fieldRequired.length; i++){
		var obj = formobj.elements[fieldRequired[i]];
		if (obj){
			switch(obj.type){
			case "select-one":
				if (obj.selectedIndex == -1 || obj.options[obj.selectedIndex].text == ""){
					alertMsg += " - " + fieldDescription[i] + "\n";
				}
				break;
			case "select-multiple":
				if (obj.selectedIndex == -1){
					alertMsg += " - " + fieldDescription[i] + "\n";
				}
				break;
			case "text":
			case "textarea":
				if (obj.value == "" || obj.value == null){
					alertMsg += " - " + fieldDescription[i] + "\n";
				}
				break;
			default:
			}
			if (obj.type == undefined){
				var blnchecked = false;
				for (var j = 0; j < obj.length; j++){
					if (obj[j].checked){
						blnchecked = true;
					}
				}
				if (!blnchecked){
					alertMsg += " - " + fieldDescription[i] + "\n";
				}
			}
		}
	}

	if (alertMsg.length == l_Msg){
		if(formobj.pin.value != formobj.validatepin.value) {
            alert ("Los números PIN introducidos no coinciden.  Vuelva a introducir la información de PIN.");
			return false;
		}
		return true;
	}else{
		alert(alertMsg);
		return false;
	}
}

function OnlineUserActivationCheck(formobj){
	// Enter name of mandatory fields
	var fieldRequired = Array("user_id", "pin", "new_user_id");
	// Enter field description to appear in the dialog box
	var fieldDescription = Array("Temporary ID", "PIN", "New User ID");
	// dialog message
	var alertMsg = "Please complete the following required fields:\n";

	var l_Msg = alertMsg.length;

	for (var i = 0; i < fieldRequired.length; i++){
		var obj = formobj.elements[fieldRequired[i]];
		if (obj){
			switch(obj.type){
			case "select-one":
				if (obj.selectedIndex == -1 || obj.options[obj.selectedIndex].text == ""){
					alertMsg += " - " + fieldDescription[i] + "\n";
				}
				break;
			case "select-multiple":
				if (obj.selectedIndex == -1){
					alertMsg += " - " + fieldDescription[i] + "\n";
				}
				break;
			case "text":
			case "textarea":
				if (obj.value == "" || obj.value == null){
					alertMsg += " - " + fieldDescription[i] + "\n";
				}
				break;
			default:
			}
			if (obj.type == undefined){
				var blnchecked = false;
				for (var j = 0; j < obj.length; j++){
					if (obj[j].checked){
						blnchecked = true;
					}
				}
				if (!blnchecked){
					alertMsg += " - " + fieldDescription[i] + "\n";
				}
			}
		}
	}

	if (alertMsg.length == l_Msg){
		return true;
	}else{
		alert(alertMsg);
		return false;
	}
}

function showTab(tabId)
{
	var myTabs = new Array();
	var myCount;
	var myObject;
	var strTab;

	myTabs[0] = "account_summary";
	myTabs[1] = "account_charges";
	myTabs[2] = "account_suspensions";
	myTabs[3] = "account_holds";
	myTabs[4] = "account_bills";
	myTabs[5] = "account_bookings";
	myTabs[6] = "account_reservations";
	myTabs[7] = "email_and_pin";

	if (tabId == "")
	  strTab = myTabs[0];
	else
	  strTab = tabId;

	// purely defensive - found a way to reach this state
	// when testing without logging in to view my account
	myObject = document.getElementById(strTab);
	if (myObject == null)
	  strTab = myTabs[0];

	sendCurrentTab(strTab);

	for (myCount = 0; myCount < myTabs.length; myCount++)
	  {
	  myObject = document.getElementById(myTabs[myCount]);
	  if (myObject != null)
	    {
	    myObject.style.display='none';
	    }
	  myObject = document.getElementById(myTabs[myCount] + '_tab');
	  if (myObject != null)
	    {
	    myObject.className='tabOff';
	    }
	  }

	myObject = document.getElementById(strTab);
	if (myObject != null)
	  myObject.style.display='block';
	myObject = document.getElementById(strTab + '_tab');
	if (myObject != null)
	  myObject.className='tab';
}

function selectAll(inForm,inBox) 
{
	var checkboxes = document.getElementById(inForm).length;

	if (document.getElementById(inBox).checked == true)
          {
	  for (i=0; i < checkboxes; i++) 
	    {
	    if (document.getElementById(inForm)[i].onclick == null &&
		document.getElementById(inForm)[i].type == "checkbox")
	      document.getElementById(inForm)[i].checked = true;
	    }
	  }
        else 
	  {
	  for (i=0; i < checkboxes; i++)
	    {
	    if (document.getElementById(inForm)[i].onclick == null && 
		document.getElementById(inForm)[i].type == "checkbox")
	      document.getElementById(inForm)[i].checked = false;
	    }
	  }
}

function NewCalHold(pCtrl,pFormat,pShowTime,pTimeMode,inCheckbox)
{
	var myCheckbox;

	myCheckbox = document.getElementById(inCheckbox);
	
	if (myCheckbox.checked != true)
	  NewCal(pCtrl,pFormat,pShowTime,pTimeMode);
}

function cancelSelected()
{
	var myCheckbox;
	var mySubmit;

	myCheckbox = document.getElementById("cancelselected");
	mySubmit = document.getElementById("submitholdsbutton");
	mySelect = document.getElementById("pickup_library");
	myExpiration = document.getElementById("hold_expiration_date");

	if (myCheckbox != null && myCheckbox.checked == true)
	  {
	  if (mySubmit != null)
	    mySubmit.value = 'Cancelar reservas seleccionadas';
	  if (mySelect != null)
	    mySelect.disabled = true;
	  if (myExpiration != null)
	    myExpiration.disabled = true;
	  }
	else
	  {
	  if (mySubmit != null)
	    mySubmit.value = 'Editar reservas seleccionadas';
	  if (mySelect != null)
	    mySelect.disabled = false;
	  if (myExpiration != null)
	    myExpiration.disabled = false;
	  }
}

function processholdform()
{
	var myCheckbox;
	var myForm;
	var checkboxes;
	var conirmeditall;
	var count;
	var editall;
	var strWork;
	var strID;
	var pieces;
	var sometoedit;
	var nFORM;
	var nField;
	var myHoldExpiration;
	var myPickupLibrary;

	myCheckbox = document.getElementById("cancelselected");

	if (myCheckbox.checked == true)
	  {
	  myForm = document.getElementById("holds_list");
	  if (myForm != null)
	    {
	    if (someChecked("holds_list"))
	      {
	      editall = allChecked("holds_list");
	      if (editall)
	        confirmeditall = confirm("Se están cambiando todas las reservas. ¿Continuar?");

	      if (!editall || (editall && confirmeditall))
	        {
	        myForm.submit();
		}
	      }
	    else
	      {
	      window.alert("Por favor, revise las reservas que desea cancelar");
	      }
	    }
	  }
	else
	  {
	  // The edit portion 
	  myForm = document.getElementById("holds_list");
	  if (myForm != null)
	    {
	    sometoedit = someChecked("holds_list");
	    if (sometoedit)
	      {
	      editall = allChecked("holds_list");
	      if (editall)
	        confirmeditall = confirm("Se están cambiando todas las reservas. ¿Continuar?");

	      if (!editall || (editall && confirmeditall))
	        {
	        myHoldExpiration = document.getElementById("hold_expiration_date").value;
	        myPickupLibrary = document.getElementById("pickup_library").value;
                nFORM=document.createElement('form');
     	        nFORM.action='/uhtbin/cgisirsi/?ps=YsDjkzlyUd/0/235110023/136';
	        nFORM.target="_self";
	        nFORM.method="post";
  	        nFORM.name="EditHolds";
	        checkboxes = myForm.length;
	        for (count = 0; count < checkboxes; count++)
	          {
	          if (myForm[count].id.indexOf("HLD") != -1)
	            {
		    if (myForm[count].checked == true)
		      {
		      strWork = myForm[count].id;
		      pieces = strWork.split("^");
		      strID = pieces[0] + "^" + pieces[5];
		      strID = strID + "^" + pieces[3] + "^" + pieces[2];
	
		      nField=document.createElement('input');
	              nField.name=strID;
	              nField.id=strID;
	              nField.value='on';
	              nField.type='hidden';

	              nFORM.appendChild(nField);
		      }
                    }
		  }
	        nField=document.createElement('input');
	        nField.name='hold_expiration_date';
	        nField.id='hold_expiration_date';
	        nField.value=myHoldExpiration;
	        nField.type='hidden';
	        nFORM.appendChild(nField);
	        nField=document.createElement('input');
	        nField.name='pickup_library';
	        nField.id='pickup_library';
	        nField.value=myPickupLibrary;
	        nField.type='hidden';
	        nFORM.appendChild(nField);
	        document.body.appendChild(nFORM);
	        nFORM.submit();
		}
	      }
	    else
	      {
	      window.alert('Revise las reservas que se desea editar');
	      }
	    }
	  }
}

function processSuspend()
{
	var myCheckbox;
	var myStartDate;
	var myEndDate;
	var myButton;

	myCheckbox = document.getElementById("activate");
	myStartDate = document.getElementById("suspend_start_date");
	myEndDate = document.getElementById("suspend_end_date");
	myButton = document.getElementById("submitactivatebutton");

	if (myCheckbox != null && myCheckbox.checked)
	  {
	  if (myStartDate != null)
	    {
	    myStartDate.disabled = true; 
	    myStartDate.value = 'NEVER';
	    }
	  if (myEndDate != null)
	    {
	    myEndDate.disabled = true; 
	    myEndDate.value = 'NEVER';
	    } 
	  if (myButton != null)
	    myButton.value = 'Activar seleccionadas';
	  }
	else
	  {
	  if (myStartDate != null)
	    {
	    myStartDate.disabled = false; 
	    myStartDate.value = "TODAY";
	    }
	  if (myEndDate != null)
	    {
	    myEndDate.disabled = false; 
	    myEndDate.value = 'NEVER';
	    } 
	  if (myButton != null)
	    myButton.value = 'Suspender seleccionadas';
	  }
}

function processactivateform()
{
	var myCheckbox;
	var myForm;
	var checkboxes;
	var count;
	var confirmeditall;
	var editall;
	var strWork;
	var strID;
	var pieces;
	var sometoedit;
	var nFORM;
	var nField;
	var myStartDate;
	var myEndDate;

	// The edit portion 
	myForm = document.getElementById("holds_list");
	if (myForm != null)
	  {
	  sometoedit = someChecked("holds_list");
	  if (sometoedit)
	    {
	    editall = allChecked("holds_list");
	    if (editall)
	      confirmeditall = confirm("Se están cambiando todas las reservas. ¿Continuar?");

	     if (!editall || (editall && confirmeditall))
	     { 

	      myStartDate = document.getElementById("suspend_start_date").value;
	      myEndDate = document.getElementById("suspend_end_date").value;
              nFORM=document.createElement('form');
     	      nFORM.action='/uhtbin/cgisirsi/?ps=nSTg1V7n71/0/235110023/136';
	      nFORM.target="_self";
	      nFORM.method="post";
  	      nFORM.name="SuspendHolds";
	      checkboxes = myForm.length;
	      for (count = 0; count < checkboxes; count++)
	        {
	        if (myForm[count].id.indexOf("HLD") != -1)
	          {
	          if (myForm[count].checked == true)
		    {
		    strWork = myForm[count].id;
		    pieces = strWork.split("^");
		    strID = pieces[0] + "^" + pieces[5];
		    strID = strID + "^" + pieces[3] + "^" + pieces[2];

		    nField=document.createElement('input');
	            nField.name=strID;
	            nField.id=strID;
	            nField.value='on';
	            nField.type='hidden';

	            nFORM.appendChild(nField);
		    }
                  }
	        }
	      nField=document.createElement('input');
	      nField.name='suspend_start_date';
	      nField.id='suspend_end_date';
	      nField.value=myStartDate;
	      nField.type='hidden';
	      nFORM.appendChild(nField);
	      nField=document.createElement('input');
	      nField.name='suspend_end_date';
	      nField.id='suspend_end_date';
	      nField.value=myEndDate;
	      nField.type='hidden';
	      nFORM.appendChild(nField);
	      document.body.appendChild(nFORM);
	      nFORM.submit();
	      }
	    }
	  else
	    {
	    window.alert('Revise las reservas que desee activar o suspender');
	    }
	  }
}

function sendCurrentTab(inTab)
{
	var myImage;
	var aImage;

	aImage = document.getElementById("settab");

	myImage = new Image();
	myImage.src = '/uhtbin/cgisirsi/?ps=aoto4DdnR7/0/235110023/148/' + inTab;
	aImage.src=myImage.src;
	myImage = new Image();
	myImage.src = '/WebCat_Images/Castellano/Other/Miscil/clear.gif';
	aImage.src=myImage.src;
}

function verifyAndSubmit(inForm)
{
	if (!someChecked(inForm))
	  ask_to_select(inForm);
	else
	  {
	  if (allChecked(inForm))
	    {
	    if (ask_for_confirmation(inForm))
	      {
	      submitForm(inForm);
	      }
	    }
	    else
	      {
	      submitForm(inForm);
	      }
	  }
}

function allChecked(inForm)
{
	var allselected = false;

	var myForm;

	myForm = document.getElementById(inForm);
	if (myForm != null)
	  {
	  allselected = true;
	  checkboxes = myForm.length;
	  for (count = 0; count < checkboxes; count++)
	    if (myForm[count].type == 'checkbox')
	      if (myForm[count].onclick == null)
	        if (myForm[count].checked == false)
		  allselected = false;
	  }

	return allselected;
}

function someChecked(inForm)
{
	var somechecked = false;
	var myForm;

	myForm = document.getElementById(inForm);
	if (myForm != null)
	  {
	  checkboxes = myForm.length;
	  for (count = 0; count < checkboxes; count++)
	    if (myForm[count].type == 'checkbox')
	      if (myForm[count].onclick == null)
	        if (myForm[count].checked == true)
		  somechecked = true;
	  }

	return somechecked;
}

function ask_to_select(inForm)
{
	var strMessage;

	strMessage = "No se ha seleccionado nada.";

	if (inForm == "renewitems")
	  strMessage = "No se seleccionaron documentos para renovar";
	if (inForm == "rsvns_list")
	  strMessage = "Compruebe las reservas que desee cancelar";

	window.alert(strMessage);
}

function ask_for_confirmation(inForm)
{
	var strMessage;

	strMessage = "Se han seleccionado todos. ¿Continuar?";

	if (inForm == "renewitems")
	  strMessage = "Se están cambiando todos los préstamos. ¿Continuar?";
	if (inForm == "avail_list")
	  strMessage = "Se está a punto de cancelar todas las reservas listas para recoger. ¿Continuar?";

	return confirm(strMessage);
}

function submitForm(inForm)
{
	var myForm;

	myForm = document.getElementById(inForm);

	if (myForm != null)
	  myForm.submit();
}

</script>


<!-- Javascript name: My Date Time Picker
 * Date created: 16-Nov-2003 23:19
 * Scripter: TengYong Ng
 * Copyright (c) 2003 TengYong Ng
 * FileName: DateTimePicker.js
 * Version: 0.8
 * Note: Permission given to use this script in ANY kind of applications if
 *        header lines are left unchanged.
 *
 * Modified by: SirsiDynix, 2004 - 2006
 --> 

<script language="JavaScript" type="text/javascript">

var winCal;
var dtToday=new Date();
var Cal;
var docCal;
var MonthName=["Enero", "Febrero", "Marzo", "Abril",
        "Mayo", "Junio", "Julio", "Ago.", "Septiembre",
        "Octubre", "Noviembre", "Diciembre"];
var WeekDayName=["Domingo","Lunes","Martes","Miércoles",
        "Jueves","Viernes","Sábado"];
var exDateTime;        /* Existing Date and Time */

/* Configurable parameters */
var cnTop="200";       /* Top coordinate of calendar window. */
var cnLeft="500";      /* Left coordinate of calendar window */
var WindowTitle ="Calendario";
var WeekChar=2;        /* Number of character for week day. If 2 
                        * then Mo,Tu,We. if 3 then Mon,Tue,Wed */
var CellWidth=20;      /* Width of day cell. */
var DateSeparator="/";
var TimeMode=24;       /* Default TimeMode value. 12 or 24 */
var ShowLongMonth=true;/* Show long month name in Calendar header. */
var ShowMonthYear=true;/* Show Month and Year in Calendar header. */
var MonthYearColor="#003366";  
var WeekHeadColor="#003366";   
var WeekendColor="#EEEEEE";   
var WeekDayColor="#FFFFFF"; 
var FontColor="#000000";         
var SelDateColor="#FFCC33";  
var ThemeBg="";        /* Background image of Calendar window. */
/* End Configurable parameters */

function NewCal(pCtrl,pFormat,pShowTime,pTimeMode)
{
	Cal=new Calendar(dtToday);
	if ((pShowTime!=null) && (pShowTime))
	{
		Cal.ShowTime=true;
		if ((pTimeMode!=null) &&((pTimeMode=='12')||(pTimeMode=='24')))
		{
			TimeMode=pTimeMode;
		}		
	}	
	if (pCtrl!=null)
		Cal.Ctrl=pCtrl;
	if (pFormat!=null)
		Cal.Format=pFormat.toUpperCase();
	
	exDateTime=document.getElementById(pCtrl).value;
	if (exDateTime!="")    /* Parse Date String */
	{
		var Sp1;       /* Index of Date Separator 1 */
		var Sp2;       /* Index of Date Separator 2 */ 
		var tSp1;      /* Index of Time Separator 1 */
		var tSp2;      /* Index of Time Separator 2 */
		var strMonth;
		var strDate;
		var strYear;
		var intMonth;
		var YearPattern;
		var strHour;
		var strMinute;
		/* Parse month */
		Sp1=exDateTime.indexOf(DateSeparator,0)
		Sp2=exDateTime.indexOf(DateSeparator,(parseInt(Sp1)+1));
		if ((Cal.Format.toUpperCase()=="DDMMYYYY") || (Cal.Format.toUpperCase()=="DDMMMYYYY"))
		{
			strMonth=exDateTime.substring(Sp1+1,Sp2);
			strDate=exDateTime.substring(0,Sp1);
		}
		else if ((Cal.Format.toUpperCase()=="MMDDYYYY") || (Cal.Format.toUpperCase()=="MMMDDYYYY"))
		{
			strMonth=exDateTime.substring(0,Sp1);
			strDate=exDateTime.substring(Sp1+1,Sp2);
		}
		else if ((Cal.Format.toUpperCase()=="YYYYMMDD") || (Cal.Format.toUpperCase()=="YYYYMMMDD"))
		{
			strMonth=exDateTime.substring(Sp1+1,Sp2);
			strDate=exDateTime.substring(Sp2+1);
		}
		if (isNaN(strMonth))
			intMonth=Cal.GetMonthIndex(strMonth);
		else
			intMonth=parseInt(strMonth,10)-1;
		if ((parseInt(intMonth,10)>=0) && (parseInt(intMonth,10)<12))
			Cal.Month=intMonth;

		/* Parse Date */
		if ((parseInt(strDate,10)<=Cal.GetMonDays()) && (parseInt(strDate,10)>=1))
			Cal.Date=strDate;

		/* Parse Year */
		if ((Cal.Format.toUpperCase()=="YYYYMMDD") || (Cal.Format.toUpperCase()=="YYYYMMMDD"))
			strYear=exDateTime.substring(0,4);
		else
			strYear=exDateTime.substring(Sp2+1,Sp2+5);
		YearPattern=/^\d{4}$/;
		if (YearPattern.test(strYear))
			Cal.Year=parseInt(strYear,10);

		/* Parse Time */
		if (Cal.ShowTime==true)
		{
			tSp1=exDateTime.indexOf(":",0)
			tSp2=exDateTime.indexOf(":",(parseInt(tSp1)+1));
			strHour=exDateTime.substring(tSp1,(tSp1)-2);
			Cal.SetHour(strHour);
			strMinute=exDateTime.substring(tSp1+1,tSp2);
			Cal.SetMinute(strMinute);
		}	
	}
	winCal=window.open("","DateTimePicker","toolbar=0,status=0,menubar=0,fullscreen=no,width=200,height=275 ,resizable=0,top="+cnTop+",left="+cnLeft);
	docCal=winCal.document;
	RenderCal();
}

function RenderCal()
{
	var vCalHeader;
	var vCalData;
	var vCalTime;
	var i;
	var j;
	var SelectStr;
	var vDayCount=0;
	var vFirstDay;

	docCal.open();
	docCal.writeln("<html><head><title>"+WindowTitle+"</title>");
	docCal.writeln("<script>winMain=window.opener;</script\>");
	docCal.writeln("</head><body background='"+ThemeBg+"' link="+FontColor+" vlink="+FontColor+"><form name='Calendar'>");

	vCalHeader="<table border=1 cellpadding=1 cellspacing=1 width='100%' align=\"center\" valign=\"top\">\n";

	/* Month Selector */
	vCalHeader+="<tr>\n<td colspan='7'><table border=0 width='100%' cellpadding=0 cellspacing=0><tr><td align='left'>\n";
	vCalHeader+="<select name=\"MonthSelector\" onChange=\"javascript:winMain.Cal.SwitchMth(this.selectedIndex);winMain.RenderCal();\">\n";
	for (i=0;i<12;i++)
	{
		if (i==Cal.Month)
			SelectStr="Selected";
		else
			SelectStr="";
		vCalHeader+="<option "+SelectStr+" value >"+MonthName[i]+"\n";
	}
	vCalHeader+="</select></td>";

	/* Year selector */
	vCalHeader+="\n<td align='right'><a href=\"javascript:winMain.Cal.DecYear();winMain.RenderCal()\"><b><font color=\""+MonthYearColor+"\"><</font></b></a><font face=\"Verdana\" color=\""+MonthYearColor+"\" size=x-small><b> "+Cal.Year+" </b></font><a href=\"javascript:winMain.Cal.IncYear();winMain.RenderCal()\"><b><font color=\""+MonthYearColor+"\">></font></b></a></td></tr></table></td>\n";
	vCalHeader+="</tr>";

	/* Calendar header shows Month and Year */
	if (ShowMonthYear)
		vCalHeader+="<tr><td colspan='7'><font face='Verdana' size='x-small' align='center' color='"+MonthYearColor+"'><b>"+Cal.GetMonthName(ShowLongMonth)+" "+Cal.Year+"</b></font></td></tr>\n";

	/* Week day header */
	vCalHeader+="<tr bgcolor="+WeekHeadColor+">";
	for (i=0;i<7;i++)
	{
		vCalHeader+="<td align='center'><font face='Verdana' color='white' size='x-small'>"+WeekDayName[i].substr(0,WeekChar)+"</font></td>";
	}
	vCalHeader+="</tr>";
	docCal.write(vCalHeader);
	
	/* Calendar detail */
	CalDate=new Date(Cal.Year,Cal.Month);
	CalDate.setDate(1);
	vFirstDay=CalDate.getDay();
	vCalData="<tr>";
	for (i=0;i<vFirstDay;i++)
	{
		vCalData=vCalData+GenCell();
		vDayCount=vDayCount+1;
	}
	for (j=1;j<=Cal.GetMonDays();j++)
	{
		var strCell;
		vDayCount=vDayCount+1;
		if ((j==dtToday.getDate())&&(Cal.Month==dtToday.getMonth())&&(Cal.Year==dtToday.getFullYear()))
			strCell=GenCell(j,true,SelDateColor);
		else
		{
			if (j==Cal.Date)
			{
				strCell=GenCell(j,true,SelDateColor);
			}
			else
			{
				if ((vDayCount%7==0) | (vDayCount+6)%7==0)
					strCell=GenCell(j,false,WeekendColor);
				else
					strCell=GenCell(j,null,WeekDayColor);
			}		
		}
		vCalData=vCalData+strCell;

		if((vDayCount%7==0)&&(j<Cal.GetMonDays()))
		{
			vCalData=vCalData+"</tr>\n<tr>";
		}
	}
	docCal.writeln(vCalData);

	/* Time picker */
	if (Cal.ShowTime)
	{
		var showHour;
		showHour=Cal.getShowHour();
		vCalTime="<tr>\n<td colspan='7' align='center'>\n<label for='hour'></label>";
		vCalTime+="<input type='text' name='hour' id='hour' maxlength=2 size=xx-small style=\"WIDTH: 22px\" value="+showHour+" onchange=\"javascript:winMain.Cal.SetHour(this.value)\">";
		vCalTime+=" : <label for='minute'></label>";
		vCalTime+="<input type='text' name='minute' id='minute' maxlength=2 size=xx-small style=\"WIDTH: 22px\" value="+Cal.Minutes+" onchange=\"javascript:winMain.Cal.SetMinute(this.value)\">";
		if (TimeMode==12)
		{
			var SelectAm =(parseInt(Cal.Hours,10)<12)? "Selected":"";
			var SelectPm =(parseInt(Cal.Hours,10)>=12)? "Selected":"";

			vCalTime+="<select name=\"ampm\" onchange=\"javascript:winMain.Cal.SetAmPm(this.options[this.selectedIndex].value);\">";
			vCalTime+="<option "+SelectAm+" value=\"AM\">AM</option>";
			vCalTime+="<option "+SelectPm+" value=\"PM\">PM<option>";
			vCalTime+="</select>";
		}	
		vCalTime+="\n</td>\n</tr>";
		docCal.write(vCalTime);
	}

	docCal.writeln("\n</table>");
	docCal.writeln("</form></body></html>");
	docCal.close();
}

/* Generate table cell with value */
function GenCell(pValue,pHighLight,pColor)
{
	var PValue;
	var PCellStr;
	var vColor;
	var vHLstr1;    /* HighLight string */
	var vHlstr2;
	var vTimeStr;
	
	if (pValue==null)
		PValue="";
	else
		PValue=pValue;
	
	if (pColor!=null)
		vColor="bgcolor=\""+pColor+"\"";
	else
		vColor="";
	if ((pHighLight!=null)&&(pHighLight))
		{vHLstr1="color='red'><b>";vHLstr2="</b>";}
	else
		{vHLstr1=">";vHLstr2="";}
	
	if (Cal.ShowTime)
	{
		vTimeStr="winMain.document.getElementById('"+Cal.Ctrl+"').value+=''+"+"winMain.Cal.getShowHour()"+"+':'+"+"winMain.Cal.Minutes";
		if (TimeMode==12)
			vTimeStr+="+' '+winMain.Cal.AMorPM";
	}	
	else
		vTimeStr="";
	PCellStr="<td "+vColor+" width="+CellWidth+" align='center'><font face='verdana' size='x-small'"+vHLstr1+PValue+vHLstr2+"</font></td>";
	PCellStr="<td "+vColor+" width="+CellWidth+" align='center'><font face='verdana' size='x-small'"+vHLstr1+"<a href=\"javascript:winMain.document.getElementById('"+Cal.Ctrl+"').value='"+Cal.FormatDate(PValue)+"';"+vTimeStr+";window.close();\">"+PValue+"</a>"+vHLstr2+"</font></td>";
	return PCellStr;
}

function Calendar(pDate,pCtrl)
{
	/* Properties */
	this.Date=pDate.getDate();     /* Selected date */
	this.Month=pDate.getMonth();   /* Selected month number */
	this.Year=pDate.getFullYear(); /* Selected year in 4 digits */
	this.Hours=pDate.getHours();
	
	if (pDate.getMinutes()<10)
		this.Minutes="0"+pDate.getMinutes();
	else
		this.Minutes=pDate.getMinutes();
	
	this.MyWindow=winCal;
	this.Ctrl=pCtrl;
	this.Format="ddMMyyyy";
	this.Separator=DateSeparator;
	this.ShowTime=false;
	if (pDate.getHours()<12)
		this.AMorPM="AM";
	else
		this.AMorPM="PM";
}

function GetMonthIndex(shortMonthName)
{
	for (i=0;i<12;i++)
	{
		if (MonthName[i].substring(0,3).toUpperCase()==shortMonthName.toUpperCase())
		{	return i;}
	}
}
Calendar.prototype.GetMonthIndex=GetMonthIndex;

function IncYear()
{	Cal.Year++;}
Calendar.prototype.IncYear=IncYear;

function DecYear()
{	Cal.Year--;}
Calendar.prototype.DecYear=DecYear;
	
function SwitchMth(intMth)
{	Cal.Month=intMth;}
Calendar.prototype.SwitchMth=SwitchMth;

function SetHour(intHour)
{	
	var MaxHour;
	var MinHour;
	if (TimeMode==24)
	{	MaxHour=23;MinHour=0}
	else if (TimeMode==12)
	{	MaxHour=12;MinHour=1}
	else
		alert("TimeMode can only be 12 or 24");
	var HourExp=new RegExp("^\\d\\d$");
	if (HourExp.test(intHour) && (parseInt(intHour,10)<=MaxHour) && (parseInt(intHour,10)>=MinHour))
	{	
		if ((TimeMode==12) && (Cal.AMorPM=="PM"))
		{
			if (parseInt(intHour,10)==12)
				Cal.Hours=12;
			else	
				Cal.Hours=parseInt(intHour,10)+12;
		}	
		else if ((TimeMode==12) && (Cal.AMorPM=="AM"))
		{
			if (intHour==12)
				intHour-=12;
			Cal.Hours=parseInt(intHour,10);
		}
		else if (TimeMode==24)
			Cal.Hours=parseInt(intHour,10);
	}
}
Calendar.prototype.SetHour=SetHour;

function SetMinute(intMin)
{
	var MinExp=new RegExp("^\\d\\d$");
	if (MinExp.test(intMin) && (intMin<60))
		Cal.Minutes=intMin;
}
Calendar.prototype.SetMinute=SetMinute;

function SetAmPm(pvalue)
{
	this.AMorPM=pvalue;
	if (pvalue=="PM")
	{
		this.Hours=(parseInt(this.Hours,10))+12;
		if (this.Hours==24)
			this.Hours=12;
	}
	else if (pvalue=="AM")
		this.Hours-=12;
}
Calendar.prototype.SetAmPm=SetAmPm;

function getShowHour()
{
	var finalHour;
    if (TimeMode==12)
    {
    	if (parseInt(this.Hours,10)==0)
		{
			this.AMorPM="AM";
			finalHour=parseInt(this.Hours,10)+12;
		}
		else if (parseInt(this.Hours,10)==12)
		{
			this.AMorPM="PM";
			finalHour=12;
		}		
		else if (this.Hours>12)
		{
			this.AMorPM="PM";
			if ((this.Hours-12)<10)
				finalHour="0"+((parseInt(this.Hours,10))-12);
			else
				finalHour=parseInt(this.Hours,10)-12;
		}
		else
		{
			this.AMorPM="AM";
			if (this.Hours<10)
				finalHour="0"+parseInt(this.Hours,10);
			else
				finalHour=this.Hours;	
		}
	}
	else if (TimeMode==24)
	{
		if (this.Hours<10)
			finalHour="0"+parseInt(this.Hours,10);
		else	
			finalHour=this.Hours;
	}	
	return finalHour;
}			
Calendar.prototype.getShowHour=getShowHour;

function GetMonthName(IsLong)
{
	var Month=MonthName[this.Month];
	if (IsLong)
		return Month;
	else
		return Month.substr(0,3);
}
Calendar.prototype.GetMonthName=GetMonthName;

function GetMonDays()             /* Get number of days in a month */
{
	var DaysInMonth=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
	if (this.IsLeapYear())
	{
		DaysInMonth[1]=29;
	}	
	return DaysInMonth[this.Month];	
}
Calendar.prototype.GetMonDays=GetMonDays;

function IsLeapYear()
{
	if ((this.Year%4)==0)
	{
		if ((this.Year%100==0) && (this.Year%400)!=0)
		{
			return false;
		}
		else
		{
			return true;
		}
	}
	else
	{
		return false;
	}
}
Calendar.prototype.IsLeapYear=IsLeapYear;

function FormatDate(pDate)
{
	if (this.ShowTime)
	{
		if (this.Format.toUpperCase()=="DDMMYYYY")
			return (pDate+DateSeparator+(this.Month+1)+DateSeparator+this.Year+",");
		else if (this.Format.toUpperCase()=="DDMMMYYYY")
			return (pDate+DateSeparator+this.GetMonthName(false)+DateSeparator+this.Year+",");
		else if (this.Format.toUpperCase()=="MMDDYYYY")
			return ((this.Month+1)+DateSeparator+pDate+DateSeparator+this.Year+",");
		else if (this.Format.toUpperCase()=="YYYYMMDD")
			return (this.Year+DateSeparator+(this.Month+1)+DateSeparator+pDate+",");
		else if (this.Format.toUpperCase()=="MMMDDYYYY")
			return (this.GetMonthName(false)+DateSeparator+pDate+DateSeparator+this.Year);
	}
	else
	{
		if (this.Format.toUpperCase()=="DDMMYYYY")
			return (pDate+DateSeparator+(this.Month+1)+DateSeparator+this.Year);
		else if (this.Format.toUpperCase()=="DDMMMYYYY")
			return (pDate+DateSeparator+this.GetMonthName(false)+DateSeparator+this.Year);
		else if (this.Format.toUpperCase()=="MMDDYYYY")
			return ((this.Month+1)+DateSeparator+pDate+DateSeparator+this.Year);
		else if (this.Format.toUpperCase()=="YYYYMMDD")
			return (this.Year+DateSeparator+(this.Month+1)+DateSeparator+pDate);
		else if (this.Format.toUpperCase()=="MMMDDYYYY")
			return (this.GetMonthName(false)+DateSeparator+pDate+DateSeparator+this.Year);
	}
}
Calendar.prototype.FormatDate=FormatDate;	

</script>

<style type="text/css">

a:link, a:active {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 11px;
	font-weight: normal;
	text-decoration: none;
	color: #006699;
}

a:visited {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 11px;
	font-weight: normal;
	text-decoration: none;
	color: #006699;
}

a:hover {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 11px;
	font-weight: normal;
	text-decoration: underline;
	color: #FF0000;
	background-color: #FFFFCC;
}

body {
	margin:-10px 0px 0px -10px;
	background-color: #FFFFFF;
	color: #000000;	
}

html body {
	margin: 10px 10px 10px 10px;
	background-color: #FFFFFF;
	color: #000000;	
}

p, td {
	font-family: Verdana, Helvetica, Arial, sans-serif;
}

th {
	font-family: Verdana, Helvetica, Arial, sans-serif;
	text-align: left;
	vertical-align: top;
}

label {
	font-family: Verdana, Helvetica, Arial, sans-serif;
	font-weight: bold;
}

legend {
	font-family: Verdana, Helvetica, Arial, sans-serif;
	font-weight: bold;
}

fieldset {
	border-style: none;
	border-width: 0px;
}

form {
	margin: 0px 0px 0px 0px;
}

ul {
	margin-left: 0px;
}

.bibinfo {
	font-family: Verdana, Helvetica, Arial, sans-serif;
	font-size: 12px;
	background-color: #FFFFFF;
	color: #000000;
	border-width: 0px;
	border-style: none;
	margin: 5px 5px 5px 5px;
	text-align: left;
	width: 100%;
}

.bibinfo2 {
	font-family: Verdana, Helvetica, Arial, sans-serif;
	font-size: 12px;
	background-color: #FFFFFF;
	color: #000000;
	margin: 10px 30px 10px 30px;
}

.summary {
	background-color: #FFFFFF;
	font-family: Verdana, Helvetica, Arial, sans-serif;
	font-size: 11px;
	color: #000000;
	border-width: 1px;
	border-style: solid;
	padding: 5px 5px 5px 5px;
	margin: 10px 5px 5px 10px;
}

.rootbarcell {
	font-family: Verdana, Helvetica, Arial, sans-serif;
	text-align: center;
	color: #FFFFFF;
	background-color: #666666;
	letter-spacing: 0px;
	margin: 5px 5px 5px 5px;
}

 /* Use these rootbar declaration for CSS2 browsers */

a:link.blastoff, a:visited.blastoff, a:active.blastoff {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 12px;
	font-weight: bold; 
	color: #FFFF99;
	background-color: #666666;
	text-decoration: none;
	white-space: nowrap;
	margin: 0px 7px 0px 7px;
}

a:hover.blastoff {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 12px;
	font-weight: bold; 
	color: #FFFFFF;
	background-color: #666666;
	text-decoration: underline;
	white-space: nowrap;
	margin: 0px 7px 0px 7px;
}
a:link.rootbar, a:visited.rootbar, a:active.rootbar {
	font-family: Verdana, Helvetica, Arial, sans-serif;
	font-size: 12px;
	font-weight: normal;
	color: #FFFFFF;
	background-color: #666666;
	text-decoration: none;
	white-space: nowrap;
	margin: 0px 7px 0px 7px;
}

a:hover.rootbar {
	font-family: Verdana, Helvetica, Arial, sans-serif;
	font-size: 12px;
	font-weight: normal;
	color: #FFFF99;
	background-color: #666666;
	text-decoration: underline;
	white-space: nowrap;
	margin: 0px 7px 0px 7px;
}



.accountstyle {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 12px;
	color: #000000;
	vertical-align: top;
}

.defaultstyle {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 12px;
	background-color: #FFFFFF;
	color: #000000;
	vertical-align: top;
}
th.defaultstyle {
	white-space: nowrap;
	text-align: right;
}


.enrichheader, .enrichheader a {
	background-color: #FFFFFF; 
	color: #996600; 
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 12px;
	font-weight: bold;
	letter-spacing: 2px;
	padding: 5px 0px 0px 0px;
}

.enrichsubheader {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 12px;
	font-weight: bold;
	letter-spacing: 2px;
}
.enrichcontent {
	background-color: #FFFFFF; 
	color: #000000; 
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 11px;
	vertical-align: top;
	padding: 0px 0px 5px 5px;
} 

.enrichmentservices {
	background-color: #FFFFFF;
	font-family: Verdana, Helvetica, Arial, sans-serif;
	font-size: 10px;
	color: #000000;
	border-width: 1px;
	border-style: solid;
	text-align: left;
}

.enrichtagline {
	font-family: Verdana, Helvetica, Arial, sans-serif;
	font-size: 10px;
	font-weight: normal;
	background-color: #FFFFFF;
	color: #888888;
}

.footer {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 10px;
	font-weight: normal; 
}

.gatewaystyle, .gatewaystyle a:link, .gatewaystyle a:visited, .gatewaystyle a:active, .gatewaystyle a:hover {
	background-color: #003366;
	color: #FFFFFF;
	margin: 0px 0px 0px 0px;
}

.header {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 11px;
	font-weight: bold;
	letter-spacing: 2px; 
	background-color: #006699;
	color: #FFFFFF;
}

div.header {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 11px;
	font-weight: bold;
	letter-spacing: 2px; 
	background-color: #006699;
	color: #FFFFFF;
	padding: 3px 3px 3px 3px;
}

.holdingsheader {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 11px;
	font-weight: bold;
	background-color: #FFFFFF;
	color: #006699;
}

.holdingslist {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 10px;
	background-color: #FFFFFF;
	color: #000000;
}

th.holdingslist {
	white-space: nowrap;
	text-align: right;
	vertical-align: top;
}

.indented {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 12px;
	background-color: #FFFFFF;
	color: #000000;
	margin-left: 10px;
	vertical-align: top;
}

.itemlisting, label.itemlisting {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 11px;
	background-color: #FFFFFF;
	color: #000000;
	vertical-align: top;
	font-weight: normal;
}

.itemlisting2, label.itemlisting2 {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 11px;
	background-color: #EFEFEF;
	color: #000000;
	vertical-align: top;
	font-weight: normal;
}

input.itemdetails {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 11px;
	background-color: #003366;
	color: #FFFFFF;
	width: 75px;
	margin: 5px 0px 5px 0px;
	display: block;
}

input.itemdetails2 {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 11px;
	background-color: #666666;
	color: #FFFFFF;
	width: 75px;
	margin: 5px 0px 5px 0px;
	display: block;
}

td.itemservices {
	background-color: #FFFFFF;
	font-family: Verdana, Helvetica, Arial, sans-serif;
	font-size: 11px;
	color: #000000;
}

div.itemservices {
	background-color: #FFFFFF;
	font-family: Verdana, Helvetica, Arial, sans-serif;
	font-size: 11px;
	color: #000000;
	text-align: left;
	border-width: 1px;
	border-style: solid;
	padding: 7px 7px 7px 7px;
	margin: 0px 0px 0px 0px;
}

div.itemservices a:link, div.itemservices a:visited, div.itemservices a:active {
	display: block;
	margin: 3px 0px 3px 0px;
}

div.itemservices a:hover {
	background-color: #FFFFCC;
	color: #FF0000;
	display: block;
	margin: 3px 0px 3px 0px;
}

.langicon {
	font-family: Verdana, Helvetica, Arial, sans-serif;
	font-size: 11px;
	text-align: center;
	background-color: #003366;
	letter-spacing: 0px; 
	padding: 0px 0px 3px 0px;
}

a.holdicon:link { 
	color: #FFFFFF;
	border-style: outset;
	border-width: thin; 
	border-color: #EEEEEE;;
	background-color: #003366;
	text-decoration: none;
	text-align: center;
	width: 73px;
	display: block;
	padding: 1px 1px 1px 1px;
	margin: 0px 0px 0px 0px;
}

a.holdicon:hover {
	color: #FFFFFF;
	border-style: outset;
	border-width: thin; 
	border-color: #EEEEEE;;
	background-color: #003366;
	text-decoration: none;
	text-align: center;
	width: 73px;
	display: block;
	padding: 1px 1px 1px 1px;
	margin: 0px 0px 0px 0px;
}

div.options {
	background-color: #FFFFFF;
	font-family: Verdana, Helvetica, Arial, sans-serif;
	font-size: 11px;
	color: #000000;
	border-width: 1px;
	border-style: solid;
	padding: 5px 5px 5px 5px;
	margin: 10px 5px 5px 10px;
}

.overdue, .error {
	color: #CC0000;
}

.pagecontainer {
	background-color: #FFFFFF;
	font-family: Verdana, Helvetica, Arial, sans-serif;
	font-size: 12px;
	color: #000000;
	border-width: 1px;
	border-style: solid;
}

.pagecontainer3pg {
	background-color: #FFFFFF;
	font-family: Verdana, Helvetica, Arial, sans-serif;
	font-size: 12px;
	color: #000000;
	border-width: 1px;
	border-style: solid;
	
}

.rsvholdings {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 10px;
	background-color: #FFFFCC;
	color: #000000;
}

.searchheader {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 12px;
	font-weight: bold;
	letter-spacing: 2px; 
	background-color: #006699;
	color: #FFFFFF;
	padding: 3px 3px 3px 3px;
	width: 100%;
}

.searchcontent {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 12px;
	background-color: #EEEEEE;
	color: #000000;
	padding: 3px 3px 3px 3px;
	vertical-align: middle;
	white-space: nowrap;
}

table.searchcontent {
	width: 99%;
}

th.searchcontent {
	text-align: right;
	width: 30%;
}


.searchservices {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 12px;
	background-color: #EEEEEE;
	color: #000000;
	border-width: 1px;
	border-style: solid;
}

input.searchbutton {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 11px;
	font-weight: bold;
	background-color: #003366;
	color: #FFFFFF;
	vertical-align: middle;
	margin: 5px;
}

a:link.searchlinks, a:active.searchlinks, a:visited.searchlinks {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 12px;
	font-weight: bold;
	text-decoration: none;
	background-color: #EEEEEE;
	color: #006699;
}

a:hover.searchlinks {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 12px;
	font-weight: bold;
	text-decoration: underline;
	background-color: #EEEEEE;
	color: #CC0000;
}

.subheader {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 12px;
	background-color: #EEEEEE;
	color: #000000;
	margin-left: 2px;
}

.sortsubheader {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 12px;
	background-color: #EEEEEE;
	color: #000000;
	margin-left: 2px;
	cursor: pointer;
	text-decoration: underline;
}

.searchsum {
	color: #000000;
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 11px;
	text-align: center;
	background-color: #FFFFFF;
}

.small {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 10px;
	font-weight: normal; 
}

.titlebar {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 14px;
	font-weight: bold;
	letter-spacing: 3px;
	background-color: #006699;
	color: #FFFFFF;
	vertical-align: top;
	padding: 3px;
}

.vreference {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 10px;
	text-decoration: none;
	font-weight: normal;
	letter-spacing: 0px;
	background-color: #006699;
	color: #FFFFFF;
}

.vreference input {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 10px;
	text-decoration: none;
	font-weight: normal;
	letter-spacing: 0px;
	background-color: #FFFFFF;
	color: #006699;
	margin: 3px 3px 3px 3px;
}

.vreference textarea {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 10px;
	text-decoration: none;
	font-weight: normal;
	letter-spacing: 0px;
	background-color: #FFFFFF;
	color: #006699;
	width: 125px;
	height: 50px;
	margin: 3px 3px 3px 3px;
}

.unformatted {
	font-family: "Courier New", Courier, monospace; 
	font-size: 12px;
	font-weight: normal; 
	vertical-align: top;
}

.viewmarcheader, .viewmarcheader a {
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 12px;
	font-weight: bold;
	letter-spacing: 2px;
	background-color: #FFFFFF;
	color: #996600;
}

.tab {
	border-top:1px solid #cccccc;
	border-right:1px solid #a9a9a9;
	margin-right:5px;
	border-left:1px solid #cccccc;
	background-color:#fefef2;
	padding:1px 4px 1px 4px;
	font-size:10pt;
}

.tabOff {
	color:#ffffff;
	background-color:#0c0575;
	background-image:url(/WebCat_Images/Castellano/Special/Link/button.png);
	background-position:top left;
	background-repeat:repeat-x;
	border-top:2px solid #050568;
	border-right:2px solid #050568;
	border-left:2px solid #050568;
	margin-right:10px;
	padding:1px 4px 1px 4px;
	font-size:10pt;
}

a.tabOff, a.tabOff:visited, a.tabOff:hover {
	color:#ffffff;
	background-color:#0c0575;
}

.panelholder {
	background-color:#fefef2;
	border-top:1px solid #cccccc;
	border-right:1px solid #a9a9a9;
	border-bottom:1px solid #a9a9a9;
	border-left:1px solid #cccccc;
	padding:10px;
	margin:0px;
}

.viewmarctags {
	vertical-align: top;
	font-family: Verdana, Helvetica, Arial, sans-serif; 
	font-size: 10px;
	background-color: #FFFFFF;
	color: #000000;
}

th.viewmarctags {
	white-space: nowrap;
	text-align: right;
	vertical-align: top;
}

.virtualreference {
	border-style: none;
	border-width: 0px;
	padding: 1px 5px 1px 5px;
}

</style>
</head>
<!-- Start the body of the document.  WARNING:  No comments are allowed inside of the body element's definition. - assign CSS Class of 'body_style' to tag -  If this is a download search results state (14, 62), then load the results in a new browser window to facilitate printing. -  If this is an Archive image view state (911), then open a new window to display the image in new window. -  To help prevent premature selection of a toolbar button (i.e., before the new toolbar is loaded), clear it when the page is unloaded. -->
<body onLoad="">

<noscript>
Your browser does not support JavaScript and this application utilizes JavaScript to build content and provide links to additional information. You should either enable JavaScript in your browser settings or use a browser that supports JavaScript in order to take full advantage of this application.
</noscript>
<!--  Copyright (c) 1996 - 2003, Sirsi Corporation - Generic top-of-page for (almost?) all pages. -->
<!--  Copyright (c) 1996 - 2008, SirsiDynix. Form for starting a new session in a new window. -->

<!-- By setting the "document.new_session.action" property to the URL for logging into a new session at the particular  page you want, a new window will be opened and a new WebCat session will be started automatically. Remember that many WebCat states are dependent on previous states, so only certain "cgi types" can be opened.

Also, by setting the "document.new_session.new_gateway_db.value" property to a gateway database name, the new session will use that gateway instead of the user's default gateway. Note that the use of Javascript is required to submit this form. -->

<form name="new_session" method="post" action="/uhtbin/cgisirsi/?ps=QsQINsdKcj/0/0/57/49" target="new_session">
  <input type="hidden" name="user_id" value="018059602">
  <input type="hidden" name="password" value="3218">
  <input type="hidden" name="new_gateway_db" value="">
</form>


<!--  Copyright (c) 2000 - 2008, SirsiDynix - Puts the top-of-page information common to all pages. -->
<a href="#skipnav"><img src="/WebCat_Images/Castellano/Other/Miscil/clear.gif" height="1" width="1" border="0" alt="Ignorar navegación" title="Ignorar navegación"></a>  <a name="top"></a>
<div class="pagecontainer"> <!-- Controls Page Border -->


<table border="0" cellpadding="3" cellspacing="0" width="100%"> <!-- title bar -->
 <tr>
  <td class="titlebar" align="left">
      <img border="0" src="/WebCat_Images/Castellano/Other/Miscil/LIBLOGO.gif" alt="" title="">
  </td>

  <td class="titlebar" align="center">
    <!-- Print the gateway envn title if not blank -->
      <!-- icon was printed -->
      Biblioteca<br>Universidad de Alicante<br><br>
   <br>
    <!-- present language choices -->
     <div align="center" class="footer">
<!-- Add the Language options -->
  <!-- Suppress an option for the current language -->
    <a href="/uhtbin/cgisirsi/?ps=uSIqUkvbcx/0/235110023/111/INGLES" title="English" target="_top"><img src="/WebCat_Images/Castellano/Other/Miscil/INGLES.gif" border=0 class="langicon" alt="&nbsp;English&nbsp;" title="English" align=center></a>
  <!-- Suppress an option for the current language -->
    <a href="/uhtbin/cgisirsi/?ps=2MEhejNeQz/0/235110023/111/CATALAN" title="Valencià" target="_top"><img src="/WebCat_Images/Castellano/Other/Miscil/CATALAN.gif" border=0 class="langicon" alt="&nbsp;Valencià&nbsp;" title="Valencià" align=center></a>
  <!-- Suppress an option for the current language -->
     </div>
  </td>
    <!-- no VIRTUAL_REF form -->
     <!-- login form-->
  <td valign="top" class="defaultstyle"><!-- container cell -->
<!--  Copyright (c) 2000 - 2006, SirsiDynix - Announcements/Activity - This page file is processed by a  SIRSI_Command for an Si response. -->
 <table border="0" cellspacing="0" cellpadding="0">
  <tr>
   <td class="enrichheader">Información de la biblioteca</td>
  </tr>
  <tr>
   <td class="enrichcontent">
	
       <a href="javascript:open_win('http://biblioteca.ua.es/es/encuentra-informacion/bibliografia-recomendada.html')">Bibliografía recomendada</a><br>
	  <!-- counter test -->
	
       <a href="/uhtbin/cgisirsi/?ps=iaR8eup0Wk/0/235110023/1/60/X">Nuevas adquisiciones</a><br>
	  <!-- counter test -->
	
       <a href="javascript:open_win('http://biblioteca.ua.es/es/estudia-y-aprende/autoaprendizaje.html')">Tutoriales</a><br>
	  <!-- counter test -->
	
       <a href="javascript:open_win('http://biblioteca.ua.es/es/utiliza-la-biblioteca/la-biblioteca-desde-casa.html')">Acceso a los recursos electrónicos desde fuera de la UA</a><br>
	  <!-- counter test -->
   </td>
  </tr>
 </table>

  </td> <!-- container cell -->	
 </tr>
</table>
<table border="0" cellpadding="3" cellspacing="0" width="100%"> <!-- title bar -->
 <tr>
  <td class="rootbarcell">
<!--  Copyright (c) 1996 - 2008, SirsiDynix - Gateway Root Bar. -->
    <!-- display text with CSS instead -->
          <a href="/uhtbin/cgisirsi/?ps=pwqtd3iv5v/0/235110023/38/1/X/BLASTOFF" class="rootbar">
       Catálogo de la biblioteca</a>
          <a href="/uhtbin/cgisirsi/?ps=Xj1SdHcCUl/0/235110023/1/2829/X/BLASTOFF" class="rootbar">
       Colección digital UA</a>
          <a href="/uhtbin/cgisirsi/?ps=T9VbDlsi2O/0/235110023/1/2830/X/BLASTOFF" class="rootbar">
       Colecciones especiales</a>
          <a href="/uhtbin/cgisirsi/?ps=BiCQWuvrF8/0/235110023/1/29/X/BLASTOFF" class="rootbar">
       Recursos electrónicos</a>
          <a href="/uhtbin/cgisirsi/?ps=W8dYV8Fips/0/235110023/1/121/X/BLASTOFF" class="rootbar">
       Servicios al usuario</a>
          <a href="/uhtbin/cgisirsi/?ps=vjf3RNU3HS/0/235110023/63/170/X/BLASTOFF" class="rootbar">
       Solicitud</a>



  </td>
 </tr>
</table>
<!--  Copyright (c) 2000 - 2008, SirsiDynix - Renew Item Selection Page; State #53 -->
<!--  Copyright (c) 2000 - 2008, SirsiDynix - Buttons for Renew Item Selection Page; State #53 -->
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="gatewaystyle">
 <tr>
  <td class="gatewaystyle">

   <!-- Go back button -->
   <a href="/uhtbin/cgisirsi/?ps=EubOq4X1Dv/0/235110023/2/5" title="VOLVER"><img src="/WebCat_Images/Castellano/Buttons/Link/GOBACK.gif" border="0" alt="VOLVER" title="VOLVER"></a>

  <!-- Help button -->
  <script language="JavaScript" type="text/javascript">
    put_help_button('Castellano','AYUDA','faq10017');
  </script>
	
  <!-- gateway's custom buttons -->

<!-- Let personal-access users create/edit their profiles -->
     <!-- don't show if not configured -->
    <a href="/uhtbin/cgisirsi/?ps=q9fxMNn22n/0/235110023/122/2005" title="Mi perfil"><img src="/WebCat_Images/Castellano/Buttons/Link/MYPROFILE.gif" border="0" alt="Mi perfil" title="Mi perfil"></a>


   <a href="/uhtbin/cgisirsi/?ps=mbWKSyDfWH/0/235110023/58" title="Desconexión" target="_top"><img src="/WebCat_Images/Castellano/Buttons/Link/EXITCAT.gif" border="0" alt="Desconexión" title="Desconexión"></a>

  </td>
 </tr>
</table>
<a name="skipnav"></a>
<table border="0" cellpadding="0" cellspacing="10" width="100%" align="center" title="" summary="This table positions all the elements on this page.">   
 <tr>
  <td> <!-- container cell -->  
  <form name="renewitems" method="post" action="/uhtbin/cgisirsi/?ps=xnAKqQn3gC/0/235110023/93">
  <input type="hidden" name="user_id" value="018059602">
   <table border="0" cellpadding="3" cellspacing="0" align="center">
    <tr>
	   <td class="header" colspan="3">Seleccionar ítems para renovar</td>
	  </tr>
		<tr>
		 <td class="subheader" colspan="3">
	  <strong>2</strong> documento/s disponible/s para renovación. Marque las casillas a continuación para marcar los ítems de la lista que desee renovar.
	   </td>
	  </tr>
		<tr>
		 <td class="defaultstyle" align="center" colspan="3">
	    <input type="radio" name="selection_type" id="renew_selected" value="selected" checked="checked">&nbsp;<label for="renew_selected">Renovar los documentos seleccionados</label>&nbsp;&nbsp;&nbsp;&nbsp;
	    <input type="radio" name="selection_type" id="renew_all" value="all">&nbsp;<label for="renew_all">Renovar todos</label>	 
	   </td>
	  </tr>
		
	  
	  
  	
	  
	    
 	  		
	  <tr>
	   <td class="itemlisting2">
		 <input type="checkbox" name="RENEW^500339510^POE 004.451/UNIX/MAR/UNI^9^Márquez García, Francisco Manuel^UNIX : programación avanzada^" id="RENEW1">
     </td>
		 <td class="itemlisting2">
		  <label for="RENEW1">
		  <!-- Print the title, if it exists -->
          UNIX : programación avanzada&nbsp;&nbsp;
		 
          <!-- Print the author, if it exists -->
          Márquez García, Francisco Manuel
		  </label>
		 </td>
		 <td class="itemlisting2" align="left">
		 devolución:
         <!-- Print the date due -->
          <strong>23/10/2017,21:00</strong><br>
		 
        </td>
	   </tr>
	   
		 
	   
	  
  	
	  
	    
	  		
	  <tr>
	   <td class="itemlisting">
		 <input type="checkbox" name="RENEW^500277013^POE 519.2(076)/REQ/CAL^3^Requena Ruiz, José^Cálculo de probabilidades : problemas resueltos^" id="RENEW2">
     </td>
		 <td class="itemlisting">
		  <label for="RENEW2">
		  <!-- Print the title, if it exists -->
          Cálculo de probabilidades : problemas resueltos&nbsp;&nbsp;
		 
          <!-- Print the author, if it exists -->
          Requena Ruiz, José
		  </label>
		 </td>
		 <td class="itemlisting" align="left">
		 devolución:
         <!-- Print the date due -->
          <strong>23/10/2017,21:00</strong><br>
		 
        </td>
	   </tr>
	   
		 
	   
	<tr>
	 <td class="defaultstyle" align="center" colspan="3">
	   <input type="submit" value="Renovar los documentos seleccionados" class="searchbutton">
		   &nbsp;&nbsp;&nbsp;&nbsp;
	   <input type="reset" value="Limpiar selección" class="searchbutton">	 
	 </td>
	</tr>
   </table>
  </form>
  </td> <!-- container cell -->
 </tr>
</table>  
<!--  Copyright (c) 2000 - 2008, SirsiDynix - Buttons for Renew Item Selection Page; State #53 -->
<table border="0" cellpadding="0" cellspacing="0" width="100%" class="gatewaystyle">
 <tr>
  <td class="gatewaystyle">

   <!-- Go back button -->
   <a href="/uhtbin/cgisirsi/?ps=QgV1nnEJTt/0/235110023/2/5" title="VOLVER"><img src="/WebCat_Images/Castellano/Buttons/Link/GOBACK.gif" border="0" alt="VOLVER" title="VOLVER"></a>

  <!-- Help button -->
  <script language="JavaScript" type="text/javascript">
    put_help_button('Castellano','AYUDA','faq10017');
  </script>
	
  <!-- gateway's custom buttons -->

<!-- Let personal-access users create/edit their profiles -->
     <!-- don't show if not configured -->
    <a href="/uhtbin/cgisirsi/?ps=7KscpJFkzE/0/235110023/122/2005" title="Mi perfil"><img src="/WebCat_Images/Castellano/Buttons/Link/MYPROFILE.gif" border="0" alt="Mi perfil" title="Mi perfil"></a>


   <a href="/uhtbin/cgisirsi/?ps=Iop22DSBRm/0/235110023/58" title="Desconexión" target="_top"><img src="/WebCat_Images/Castellano/Buttons/Link/EXITCAT.gif" border="0" alt="Desconexión" title="Desconexión"></a>

  </td>
 </tr>
</table>
<a name="skipnav"></a>
<br>
<!--  Copyright (c) 1996 - 2009, SirsiDynix - Copyright statement -->
<table border="0" cellpadding="3" cellspacing="0" width="100%" class="footer">
 <tr>
  <td align="center" valign="bottom" width="15%" class="footer">
      <img src="/WebCat_Images/Castellano/Other/Miscil/sirsi_button.gif" alt="Powered by: SirsiDynix" border="0">
  </td>
  <td align="center" class="footer"><!-- Display the description -->

   Biblioteca<br>Universidad de Alicante<br><br><br> 
   <br>
     Copyright &#169; 2000 - 2009, SirsiDynix
  </td>
  <td align="center" width="15%" class="footer"><a name="bottom" href="#top">ARRIBA</a></td>
 </tr>
</table>
</div> <!-- Controls Page Border -->
</body>
</html>
'''


testPageMultiLocations = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<!--  Copyright (c) 2000 - 2008, Sirsi Corporation - Defines the head  body of each page. -->
<html lang="es" dir="ltr"><head>
	
	
	
		<title>iLink Universidad de Alicante</title>
	
	
	<!-- Set the expiration date to the past so the page will always be reloaded -->
		<meta http-equiv="Expires" content="Sun, 1 Jan 1995 08:00:00 CST">
	
		<!-- Not the login page -->
	
	<!--  Copyright (c) 1997 - 2008, SirsiDynix - JavaScript functions defined in every page. -->
	<script language="JavaScript" type="text/javascript">
	
	// used by dynamic table sorting
	var currentCol = 0;
	
	function open_win(url) {
		new_win = window.open(url,"new_win",'toolbar=1,location=1,directories=0,status=1,menubar=1,scrollbars=1,resizable=1,width=750,height=250');
		if (new_win)
		{
			new_win.focus();
		}
	}
	
	function open_bare_win(url) {
		new_b_win = window.open(url,"new_b_win",'toolbar=0,location=0,directories=0,status=1,menubar=0,scrollbars=1,resizable=1,width=620,height=450');
		if (new_win)
		{
			new_b_win.focus();
		}
	}
	
	function open_hyperion_image_win(url) {
		hyperion_image_win = window.open(url,"hyperion_image_win",'toolbar=0,location=0,directories=0,status=1,menubar=0,scrollbars=1,resizable=1,width=600,height=450,screenX=410,screenY=210');
	}
	
	function open_hyperion_info_win(url) {
		hyperion_info_win = window.open(url,"hyperion_info_win",'toolbar=0,location=0,directories=0,status=1,menubar=0,scrollbars=1,resizable=1,width=400,height=450,screenX=0,screenY=210');
	}
	
	function open_win_timeout(url,timeout) {
		new_win = window.open(url,"new_win",'toolbar=0,location=0,directories=0,status=1,menubar=1,scrollbars=1,resizable=1,width=750,height=250');
		setTimeout("new_win.close()",timeout);
	}
	
	function open_help_win(url) {
		new_win = window.open(url,"help_win",'toolbar=0,location=0,directories=0,status=1,menubar=0,scrollbars=1,resizable=1,width=640,height=480');
		if (new_win)
		{
			new_win.focus();
		}
	}
	
	function open_bounce_win(url) {
		new_win = window.open(url,"bounce_win",'toolbar=0,location=0,directories=0,status=1,menubar=0,scrollbars=1,resizable=1,width=620,height=450');
	}
	
	/* Function for icon-type search form action */
	function orig_form_action()
	{
		if (!document.searchform.search_type[0].checked)
			{
			return true;
			}
		else
			{
						document.url_form.url.value = "http://www.google.com/search?q=" + document.searchform.searchdata1.value + "&safe=vss&vss=1&sa=Google+Search";
						open_win(document.url_form.url.value);
			return false;
			}
	}
	
	function combine_fields()
	{
			document.getElementById("searchdata3").value="{LEXILE}>" + document.getElementById("lexilemin").value + "<" + document.getElementById("lexilemax").value;
			//alert (document.getElementById("searchdata3").value);
	}
	
	/* Function for icon-type search form action */
	function search_form_action()
	{
		var search_engine_checked = 0;
		var temp_str;
	
		for (var i = 0; i < document.searchform.search_type.length; i++)
			{
			if (document.searchform.search_type[i].value == "searchengine")
				if (document.searchform.search_type[i].checked)
					search_engine_checked = 1;
			}
	
		if (!search_engine_checked)
			{
			return true;
			}
		else
			{
						temp_str = document.searchform.searchdata1.value;
			temp_str = temp_str.replace(/\s+/g,"+");
						document.url_form.url.value = "http://www.google.com/search?q=" + temp_str + "&safe=vss&vss=1&sa=Google+Search";
						open_win(document.url_form.url.value);
			return false;
			}
	}
	
	function getNonJavaHelpFileUrl(langDir, file)
	{
		if (file == "ibistro_overview") {
			return '/iBistro_helps/User/' + langDir + '/index.htm';
		}
		else {
			return '/iBistro_helps/User/' + langDir + '/index.htm?context=elibrary&topic=' + file;
		}
	}
	
	
	function put_help_button(langDir, alttextHelp, file)
	{
		document.writeln('<a href="#" onclick="javascript:open_help_win(\''+getNonJavaHelpFileUrl(langDir,file)+'\')" alt="'+alttextHelp+'" title="'+alttextHelp+'">'+'<img src="/WebCat_Images/Castellano/Buttons/Link/HELP.gif" border="0" alt="AYUDA"  title="AYUDA">'+'<\/a>');
	}
	
	
	function put_keepremove_button(ckey,value)
	{
		document.writeln('<img name="ickey-' + ckey + '"');
		document.writeln('src="/WebCat_Images/Castellano/Other/Miscil/clear.gif"');
		document.writeln('alt="' + value + '" border="0">');
	
		document.writeln('<input type="button"');
		if (value == 'Guardar')
			{
			document.writeln('class="itemdetails"');
			}
		else
			{
			document.writeln('class="itemdetails2"');
			}
		document.writeln('name="ckey-' + ckey + '"');
		document.writeln('id="ckey-' + ckey + '"');
		document.writeln('value="' + value + '" alt="' + value + '"');
		document.writeln('onClick="javascript:updatekeptlist(this,' + ckey + ');">');
	}
	
	function updatekeptlist(myButton,ckey)
	{
		key = "i" + myButton.name;
		if (myButton.value == 'Guardar')
			{
			myImage = new Image();
			myImage.src = '/uhtbin/cgisirsi/?ps=GNyaoE1rjx/x/165390243/125/ADD?kept-' + ckey + '=on';
			document.images[key].src=myImage.src;
			myImage = new Image();
			myImage.src = '/WebCat_Images/Castellano/Other/Miscil/clear.gif';
			document.images[key].src=myImage.src;
			document.images[key].alt='Suprimir';
			myButton.value='Suprimir';
			myButton.className='itemdetails2';
			}
		else
			{
			myImage = new Image();
			myImage.src = '/uhtbin/cgisirsi/?ps=iKef6bykBY/x/165390243/125/REMOVE?kept-' + ckey + '=on';
			document.images[key].src=myImage.src;
			myImage = new Image();
			myImage.src = '/WebCat_Images/Castellano/Other/Miscil/clear.gif';
			document.images[key].src=myImage.src;
			document.images[key].alt='Guardar';
			myButton.value='Guardar';
			myButton.className='itemdetails';
		}
	}
	
	
	function put_keepremove_all_button()
	{
		document.writeln('<img name="ckey-ALL"');
		document.writeln('src="/WebCat_Images/Castellano/Other/Miscil/clear.gif"');
		document.writeln('alt="' + 'Guardar página' + '" border="0">');
	
		document.writeln('<input type="button"');
		document.writeln('class="itemdetails"');
		document.writeln('style="width: 145;"');
		document.writeln('name="ckey-ALL"');
		document.writeln('value="' + 'Guardar página' + '" alt="' + 'Guardar página' + '"');
		document.writeln('onClick="javascript:updatekeptlist_all(this,keep_ckeys_array);">');
	}
	
	function updatekeptlist_all(myButton,ckeys_array)
	{
		var ckey_str = new String("");
	
		for (i=0; i<ckeys_array.length; i++)
		{
			ckey_str = ckey_str + "kept-" + ckeys_array[i] + "=on&";
		}
		key = myButton.name;
		myImage = new Image();
		myImage.src = '/uhtbin/cgisirsi/?ps=b1WCMks3Kk/x/165390243/125/ADD?' + ckey_str;
		document.images[key].src=myImage.src;
	
		// Change all individual Keep buttons to "marked"
		for (i=0; i<ckeys_array.length; i++)
		{
			ckey = ckeys_array[i];
			element_id = "ckey-" + ckey;
			document.images["i" + element_id].alt='Suprimir';
			document.getElementById(element_id).value='Suprimir';
			document.getElementById(element_id).className='itemdetails2';
		}
		myImage = new Image();
		myImage.src = '/WebCat_Images/Castellano/Other/Miscil/clear.gif';
		document.images[key].src=myImage.src;
	}
	
	function do_history(form)
		{
		// Based on the value of the srch_history <select> list, set the search input fields.
		var opt_idx;
		var i = 0;
		opt_idx = form.srch_history.selectedIndex;
		// The history "value" is formatted:  "term^label^library"
		valueArray = form.srch_history.options[opt_idx].value.split("^");
		// Set the search term
		form.searchdata1.value = valueArray[0];
		// Set the search type - if it is present
		if (form.srchfield1 != null)
			{
			for (i<0; i<form.srchfield1.length; i++)
				{
				if (form.srchfield1.options[i].text == valueArray[1])
					{
					form.srchfield1.options[i].selected = true;
					break;
					}
				}
			}
		// Set the library
		form.library.value = valueArray[2];
		}
	
	
	
	function sendOpenURL(inISBN,inTITLE,inISSN,inGENRE)
	{
		aWindow = window.open('','','toolbar=1,location=1,directories=0,status=1,menubar=1,scrollbars=1,resizable=1,width=750,height=250');
		
		if (aWindow.document.body == null)
			{
			aBody = aWindow.document.createElement('body');
			aWindow.document.appendChild(aBody);
			}
	
					nFORM=aWindow.document.createElement('form');
		nFORM.action='';
		nFORM.target="_self";
		nFORM.method="post";
		nFORM.name="OpenURL";
	
		if (inISBN.length != 0)
			{
			nISBN=aWindow.document.createElement('input');
			nISBN.name='isbn';
			nISBN.value=inISBN;
			nISBN.type='hidden';
	
			nFORM.appendChild(nISBN);
			}
	
		if (inTITLE.length != 0)
			{
			nTITLE=aWindow.document.createElement('input');
			nTITLE.name='title';
			nTITLE.value=inTITLE;
			nTITLE.type='hidden';
	
			nFORM.appendChild(nTITLE);
			} 
	
		if (inISSN.length != 0)
			{
			nISSN=aWindow.document.createElement('input');
			nISSN.name='issn';
			nISSN.value=inISSN;
			nISSN.type='hidden';
	
			nFORM.appendChild(nISSN);
			}
	
		if (inGENRE.length != 0)
			{
			nGENRE=aWindow.document.createElement('input');
			nGENRE.name='genre';
			nGENRE.value=inGENRE;
			nGENRE.type='hidden';
	
			nFORM.appendChild(nGENRE);
			}
	
		aWindow.document.body.appendChild(nFORM);
	
		nFORM.submit();
	
		aWindow.document.body.removeChild(nFORM);
	
	}
	
	function sendEnvisionWare(inUser,inPassword)
	{
		aWindow = window.open('','','toolbar=1,location=1,directories=0,status=1,menubar=1,scrollbars=1,resizable=1,width=750,height=250');
		
		if (aWindow.document.body == null)
			{
			aBody = aWindow.document.createElement('body');
			aWindow.document.appendChild(aBody);
			}
	
		if (1 == 1)
			strPassword = '';
		else
						strPassword = inPassword;
	
					nFORM=aWindow.document.createElement('form');
		nFORM.action='';
		nFORM.target="_self";
		nFORM.method="post";
		nFORM.name="EnvisionWare";
		
		nuid=aWindow.document.createElement('input');
		nuid.id='user_id';
		nuid.name='user_id';
		nuid.value=inUser;
		nuid.type='hidden';
	
		nFORM.appendChild(nuid);
	
		npassword=aWindow.document.createElement('input');
		npassword.id='password';
		npassword.name='password';
		npassword.value=strPassword;
		npassword.type='hidden';
	
		nFORM.appendChild(npassword);
	
		aWindow.document.body.appendChild(nFORM);
	
		nFORM.submit();
	
		aWindow.document.body.removeChild(nFORM);
	}
	
	function sendAxis(inUser,inLibrary,inBill,inTotal,inAmount)
	{
	
		currencyStr = 'E';
	
		if (currencyStr == "$")
			{
			currencyStr = "\\" + currencyStr;  
			}
	
		re = new RegExp(currencyStr,"g");
	
		inTotal = inTotal.replace(re,"");
	
		inAmount = inAmount.replace(re,"");
	
		strTotal = inTotal;
		strAmount = inAmount;
	
		strTotal = strTotal.replace(".","");
		strAmount = strAmount.replace(".","");
	
		strRef = inUser + '|' + inLibrary + '|';
		strRef = strRef + inBill + '|' + strTotal + '|';
		strRef = strRef + strAmount;
	
		// convert the strings to numbers and 
					// test for minimum before opening window
		
		if (inAmount.indexOf(",") == -1)
			{
			floatAmount = parseFloat(inAmount);
			}
		else
			{
				floatAmount = 0.0;
				workstr = inAmount;
				while (workstr.indexOf(",") != -1)
					{
			partialstr = workstr.substr(0,workstr.indexOf(","));
			floatAmount = floatAmount + parseFloat(partialstr);
			workstr = workstr.substr(workstr.indexOf(",") + 1);
					}
				floatAmount = floatAmount + parseFloat(workstr);
			}
	
		floatAmount = Math.round(floatAmount*100)/100;
	
		aWindow = window.open('','','toolbar=1,location=1,directories=0,status=1,menubar=1,scrollbars=1,resizable=1,width=750,height=250');
		
		if (aWindow.document.body == null)
			{
			aBody = aWindow.document.createElement('body');
			aWindow.document.appendChild(aBody);
			}
	
					nFORM=aWindow.document.createElement('form');
		nFORM.action='';
		nFORM.target="_self";
		nFORM.method="post";
		nFORM.name="AXIS";
	
		nRequid=aWindow.document.createElement('input');
		nRequid.name='requid';
		nRequid.value=strRef;
		nRequid.type='hidden';
	
		nFORM.appendChild(nRequid);
		
		nAmount=aWindow.document.createElement('input');
		nAmount.name='amt';
		nAmount.value=floatAmount;
		nAmount.type='hidden';
	
		while((nAmount.value.length - nAmount.value.indexOf(".")) < 3)
			{
						nAmount.value = nAmount.value + "0";
			}
	
		nFORM.appendChild(nAmount);
		
		nReturnURL=aWindow.document.createElement('input');
		nReturnURL.name='rurl';
		nReturnURL.value='';
		nReturnURL.type='hidden';
	
		nFORM.appendChild(nReturnURL);
		
		nBackURL=aWindow.document.createElement('input');
		nBackURL.name='back.url';
		nBackURL.value='';
		nBackURL.type='hidden';
	
		nFORM.appendChild(nBackURL);
	
		nSource=aWindow.document.createElement('input');
		nSource.name='source';
		nSource.value='I';
		nSource.type='hidden';
	
		nFORM.appendChild(nSource);
		
		nFundCode=aWindow.document.createElement('input');
		nFundCode.name='fund.code';
		nFundCode.value='';
		nFundCode.type='hidden';
	
		nFORM.appendChild(nFundCode);
		
		nFundName=aWindow.document.createElement('input');
		nFundName.name='fund.name';
		nFundName.value='';
		nFundName.type='hidden';
	
		nFORM.appendChild(nFundName);
		
		nRefNumber=aWindow.document.createElement('input');
		nRefNumber.name='ref';
		nRefNumber.value='';
		nRefNumber.type='hidden';
	
		nFORM.appendChild(nRefNumber);
		
		nRefNumberTwo=aWindow.document.createElement('input');
		nRefNumberTwo.name='ref2';
		nRefNumberTwo.value='';
		nRefNumberTwo.type='hidden';
	
		nFORM.appendChild(nRefNumberTwo);
		
		aWindow.document.body.appendChild(nFORM);
	
		nFORM.submit();
	
		aWindow.document.body.removeChild(nFORM);
	}
	
	function sendPayPal(inUser,inLibrary,inBill,inTotal,inAmount,inBillUser)
	{
	
		currencyStr = 'E';
	
		if (currencyStr == "$")
			{
			currencyStr = "\\" + currencyStr;  
			}
	
		re = new RegExp(currencyStr,"g");
	
		inTotal = inTotal.replace(re,"");
	
		inAmount = inAmount.replace(re,"");
	
		// convert the strings to numbers and 
					// test for minimum before opening window
		
		if (inAmount.indexOf(",") == -1)
			{
			floatAmount = parseFloat(inAmount);
			}
		else
			{
				floatAmount = 0.0;
				workstr = inAmount;
				while (workstr.indexOf(",") != -1)
					{
			partialstr = workstr.substr(0,workstr.indexOf(","));
			floatAmount = floatAmount + parseFloat(partialstr);
			workstr = workstr.substr(workstr.indexOf(",") + 1);
					}
				floatAmount = floatAmount + parseFloat(workstr);
			}
	
		floatAmount = Math.round(floatAmount*100)/100;
	
		floatMinimum = parseFloat(0);
	
		if (floatAmount < floatMinimum)
			{
				alert ("La cantidad adeudada es menor que el mínimo para utilizar PayPal");
				return;
			}	  
		
		aWindow = window.open('','','toolbar=1,location=1,directories=0,status=1,menubar=1,scrollbars=1,resizable=1,width=750,height=250');
		
		if (aWindow.document.body == null)
			{
			aBody = aWindow.document.createElement('body');
			aWindow.document.appendChild(aBody);
			}
	
	
					nFORM=aWindow.document.createElement('form');
		nFORM.action='';
		nFORM.target="_self";
		nFORM.method="post";
		nFORM.name="PayPal";
	
		nCustom=aWindow.document.createElement('input');
		nCustom.name='custom';
		nCustom.value='user=' + inUser + '&';
		nCustom.value=nCustom.value + 'library=' + inLibrary + '&';
		nCustom.value=nCustom.value + 'bill_number=' + inBill + '&';
		nCustom.value=nCustom.value + 'total_owed=' + inTotal + '&';
		nCustom.value=nCustom.value + 'amount_paid=' + inAmount + '&';
		nCustom.value=nCustom.value + 'bill_user_id=' + inBillUser;
		nCustom.type='hidden';
	
		nFORM.appendChild(nCustom);
	
		nAmount=aWindow.document.createElement('input');
		nAmount.name='amount';
		nAmount.value=floatAmount;
		nAmount.type='hidden';
	
		nFORM.appendChild(nAmount);
		
		nCmd=aWindow.document.createElement('input');
		nCmd.name='cmd';
		nCmd.value='_xclick';
		nCmd.type='hidden';
	
		nFORM.appendChild(nCmd);
		
		nBusiness=aWindow.document.createElement('input');
		nBusiness.name='business';
		nBusiness.value='';
		nBusiness.type='hidden';
	
		nFORM.appendChild(nBusiness);
		
		nItemName=aWindow.document.createElement('input');
		nItemName.name='item_name';
		nItemName.value='bill payment';
		nItemName.type='hidden';
	
		nFORM.appendChild(nItemName);
		
		nNotifyURL=aWindow.document.createElement('input');
		nNotifyURL.name='notify_url';
		nNotifyURL.value='';
		nNotifyURL.type='hidden';
	
		nFORM.appendChild(nNotifyURL);
		
		nCurrencyCode=aWindow.document.createElement('input');
		nCurrencyCode.name='currency_code';
		nCurrencyCode.value='USD';
		nCurrencyCode.type='hidden';
	
		nFORM.appendChild(nCurrencyCode);
	
		aWindow.document.body.appendChild(nFORM);
	
		nFORM.submit();
	
		aWindow.document.body.removeChild(nFORM);
	}
	
	function clearCreditCardFields()
	{
		ouracct_number=document.getElementById("acct_number");
		ouracct_name=document.getElementById("acct_name");
		ourexp_date=document.getElementById("exp_date");
		ouracct_number.value="";
		ouracct_name.value="";
		ourexp_date.value="";
	}
	
	function submitVeriSign(inUser,inData)
	{
		nFORM=document.createElement('form');
		document.body.appendChild(nFORM);
		nFORM.action='/uhtbin/cgisirsi/?ps=yY3bzKrqvT/x/165390243/144';
		nFORM.target="_self";
		nFORM.method="post";
		nFORM.name="Payment";
		
		nUser=document.createElement('input');
		nUser.name='user_id';
		nUser.value=inUser;
		nUser.type='hidden';
	
		nFORM.appendChild(nUser);
	
		nData=document.createElement('input');
		nData.name='data';
		nData.value=inData;
		nData.type='hidden';
	
		nFORM.appendChild(nData);
	
		nFORM.submit();
	}
	
	function OpenGateway(inURL,inGateway)
	{
		var need_to_replace = 0;
	
		
			need_to_replace = 1;
		
		if (need_to_replace)
			{
			inURL = inURL.replace(":///","://"+location.host+"/");
			}
	
		aWindow = window.open('','','toolbar=0,location=0,directories=0,status=1,menubar=0,scrollbars=1,resizable=1,width=600,height=600');
	
		inUserId = 'WEBSERVER';
		inPassword = '';
	
		if (aWindow.document.body == null)
			{
			aBody = aWindow.document.createElement('body');
			aWindow.document.appendChild(aBody);
			}
	
					nFORM=aWindow.document.createElement('form');
		nFORM.action=inURL;
		nFORM.target="_self";
		nFORM.method="post";
		nFORM.name="Gateway";
	
		if (inGateway.length != 0)
			{
			nGateway=aWindow.document.createElement('input');
			nGateway.name='new_gateway_db';
			nGateway.value=inGateway;
			nGateway.type='hidden';
	
			nFORM.appendChild(nGateway);
			}
	
		if (inUserId.length != 0)
			{
			nUser=aWindow.document.createElement('input');
			nUser.name='user_id';
			nUser.value=inUserId;
			nUser.type='hidden';
	
			nFORM.appendChild(nUser);
			} 
	
		if (inPassword.length != 0)
			{
			nPIN=aWindow.document.createElement('input');
			nPIN.name='password';
			nPIN.value=inPassword;
			nPIN.type='hidden';
	
			nFORM.appendChild(nPIN);
			}
	
		aWindow.document.body.appendChild(nFORM);
	
		nFORM.submit();
	
		aWindow.document.body.removeChild(nFORM);
	
	}
	
	function stripLeading(inString)
	{
		while (inString.indexOf(" ") == 0 || inString.indexOf("\n") == 0 || inString.indexOf("\t") == 0)
			{
			inString = inString.substr(1);
			}
	
		return inString;
	}
	
	function removeExtra(inString)
	{
		 inString = inString.replace(/<(.|\n)+?>/g,"");
		 inString = inString.replace(/ /g,"");
		 inString = inString.replace(/\n/g,"");
	
		 return inString;
	}
	
	function pullAmount(inString)
	{
		var reMoney;
		var result;
		var strWork;
		var portion;
	
		reMoney = new RegExp("^\\E\\d+(\\.\\d\\d)?$");
		result = reMoney.exec(inString);
		if (!reMoney.test(inString))
			{
			result = "$0.00,";
			}
		strWork = new String(result);
		strWork = strWork.replace(/\E/g,"");
		portion = strWork.split(",");
		inString = portion[0];
	
		return inString;
	}
	
	function CompareAlpha(a, b)
	{
		var strA = a[currentCol].toLowerCase();
		var strB = b[currentCol].toLowerCase();
		var pieces;
		var i;
		var reDontConsider;
		// remove html wrappers to sort the title
		strA = strA.replace(/<(.|\n)+?>/g,"");
		strB = strB.replace(/<(.|\n)+?>/g,"");
		// remove items we don't want the sort to consider
		var strDontConsider = '\\bthe\\b,\\ba\\b,\\ban\\b,\\",\\t,\\n';
		pieces = strDontConsider.split(",");
		for (i = 0; i < pieces.length; i++)
			{
			reDontConsider = new RegExp(pieces[i],"g");
			strA = strA.replace(reDontConsider,"");
			strB = strB.replace(reDontConsider,""); 
			}
		strA = stripLeading(strA);
		strB = stripLeading(strB);
		if (strA < strB) { return -1; }
		else
			{
			if (strA > strB) { return 1; }
			else { return 0; }
			}
	}
	
	function CompareDate(a, b)
	{
		var pattern;
		var pieces;
		var result;
		var workdate;
		var portion;
		var datetype;
		var dateone;
		var datetwo;
		var workstring;
	
		datetype = 1; 
	
		switch(datetype)
			{
			case 0:
					// American style dates MM/DD/YYYY
					pattern = new RegExp("([1-9]|0[1-9]|1[012])[/]([1-9]|0[1-9]|[12][0-9]|3[01])[/](19|20)\\d\\d");
					result = pattern.exec(a[currentCol]);
					if (!pattern.test(a[currentCol]))
						result = "01/01/2035";
					workdate = new String(result);
					portion = workdate.split(",");
					dateone = new Date(portion[0]);
					result = pattern.exec(b[currentCol]);
					if (!pattern.test(b[currentCol]))
						result = "01/01/2035";
					workdate = new String(result);
					portion = workdate.split(",");
					datetwo = new Date(portion[0]);
					break;
			case 1:
					// European style date DD/MM/YYYY
					pattern = new RegExp("([1-9]|0[1-9]|[12][0-9]|3[01])[/]([1-9]|0[1-9]|1[012])[/](19|20)\\d\\d");
					result = pattern.exec(a[currentCol]);
					if (!pattern.test(a[currentCol]))
						result = "01/01/2035";
					workdate = new String(result);
					portion = workdate.split(",");
					workstring = new String(portion);
					pieces = workstring.split("/");
					dateone = new Date();
					dateone.setDate(parseInt(pieces[0]));
					dateone.setMonth(parseInt(pieces[1]) - 1);
					dateone.setFullYear(parseInt(pieces[2]));
					result = pattern.exec(b[currentCol]);
					if (!pattern.test(b[currentCol]))
						result = "01/01/2035";
					workdate = new String(result);
					portion = workdate.split(",");
					workstring = new String(portion);
					pieces = workstring.split("/");
					datetwo = new Date();
					datetwo.setDate(parseInt(pieces[0]));
					datetwo.setMonth(parseInt(pieces[1]) - 1);
					datetwo.setFullYear(parseInt(pieces[2]));
					break;
			case 2:
					// Asian style dates YYYY/MM/DD
					pattern = new RegExp("(19|20)\\d\\d[/]([1-9]|0[1-9]|1[012])[/](0[1-9]|[12][0-9]|3[01]|[1-9])");
					result = pattern.exec(a[currentCol]);
					if (!pattern.test(a[currentCol]))
			result = "2035/01/01,";
					workdate = new String(result);
					portion = workdate.split(",");
					workstring = new String(portion);
					pieces = workstring.split("/");
					dateone = new Date();
					dateone.setDate(parseInt(pieces[2]));
					dateone.setMonth(parseInt(pieces[1]) - 1);
					dateone.setFullYear(parseInt(pieces[0]));
					result = pattern.exec(b[currentCol]);
					if (!pattern.test(b[currentCol]))
			result = "2035/01/01,";
					workdate = new String(result);
					portion = workdate.split(",");
					workstring = new String(portion);
					pieces = workstring.split("/");
					datetwo = new Date();
					datetwo.setDate(parseInt(pieces[2]));
					datetwo.setMonth(parseInt(pieces[1]) - 1);
					datetwo.setFullYear(parseInt(pieces[0]));
					break;
			default:
					dateone = new Date();
					datetwo = new Date();
					break;
			}
	
		if (dateone < datetwo) { return -1; }
		else
			{
			if (dateone > datetwo) { return 1; }
			else { return 0; }
			}
	}
	
	function CompareNumeric(a, b)
	{
		var numA = a[currentCol];
		var numB = b[currentCol];
	
		numA = stripLeading(numA);
		numA = removeExtra(numA);
		numA = parseInt(numA);
		if (isNaN(numA))
			numA = 0;
	
		numB = stripLeading(numB);
		numB = removeExtra(numB);
		numB = parseInt(numB);
		if (isNaN(numB))
			numB = 0;
	
					return numA - numB; 
	}
	
	function CompareMoney(a, b)
	{
		var numA = a[currentCol];
		var numB = b[currentCol];
	
		numA = stripLeading(numA);
		numA = removeExtra(numA);
		numB = stripLeading(numB);
		numB = removeExtra(numB);
		numA = pullAmount(numA);
		numB = pullAmount(numB);
	
		numA = parseFloat(numA);
		numB = parseFloat(numB);
	
		numA = numA * 100;
		numB = numB * 100;
	
		numA = Math.round(numA);
		numB = Math.round(numB);
	
		if (isNaN(numA)) { return 0;}
		else
			{
			if (isNaN(numB)) { return 0; }
			else { return numA - numB; }
			}
	}
	function TableSort(myTable, myCallingObject, myType)
	{
		// this function will determine the column number for
		// rectangular tables that have one column header
		// for each column.
		var aColumn = myCallingObject.cellIndex;
		TableSortByColumn(myTable, aColumn, myType, myCallingObject, 1);
	}
	
	function switchImage(myCallingObject)
	{
		var aColumn = myCallingObject;
		var aPath = '/WebCat_Images/Castellano/Special/Link';
		var reImage;
		var result;
		
		var strTemp;
	
		strTemp = myCallingObject.innerHTML;
	
		// check if arrow is up or down
		reImage = new RegExp("DOWN.gif\">");
		if (!reImage.test(strTemp))
			result = 1;
		else
			result = 0;
	
		// remove the current image string
		strTemp = strTemp.replace(/<img src(.|\n)+?>/gi,"");
	
		if (result == 0)
			{
			strTemp = "<img src=\"" + aPath + "/UP.gif\"> " + strTemp;
			}
		else
			{
			strTemp = "<img src=\"" + aPath + "/DOWN.gif\"> " + strTemp;
			}
	
		myCallingObject.innerHTML = strTemp;
	}
	
	function setImageDown(myCallingObject, myStepBack)
	{
		var aColumn = myCallingObject;
		var aPath = '/WebCat_Images/Castellano/Special/Link';
		var aRow;
		var aTableSection;
		var myCells;
		var myChildren;
		var myCount;
		var myCountToo;
	
		var strTemp;
		var strWork;
		
		strTemp = myCallingObject.innerHTML;
	
		if (myStepBack == 1)
			{
			// remove images from all columns
			aRow = myCallingObject.parentNode;
			myCells = aRow.childNodes;
			for (myCount = 0; myCount < myCells.length; myCount++)
				{
				if (strTemp != myCells[myCount].innerHTML)
					{
					strWork = myCells[myCount].innerHTML;
					if (strWork != null)
						{
						strWork = strWork.replace(/<img src(.|\n)+?>/gi,"");
						myCells[myCount].innerHTML = strWork;
			}
					}
				}
			}
		else
			{
			// have to get all rows in the multiple level column headers
			aTableSection = myCallingObject.parentNode.parentNode;
			myCells = aTableSection.childNodes;
			for (myCount = 0; myCount < myCells.length; myCount++)
				{
				if (myCells[myCount] != null)
					{
					if (myCells[myCount].nodeType == 1)
						{
			myChildren = myCells[myCount].childNodes;
			for (myCountToo = 0; myCountToo < myChildren.length; myCountToo++)
				{
				if (myChildren[myCountToo] != null && 
						myChildren[myCountToo].nodeType == 1)
					{
								if (strTemp != myChildren[myCountToo].innerHTML)
									{
									strWork = myChildren[myCountToo].innerHTML;
									if (strWork != null)
										{
										strWork = strWork.replace(/<img src(.|\n)+?>/gi,"");
										myChildren[myCountToo].innerHTML = strWork;
							}
									}
					}
							}
						}
					}
				}
			}
	
		strTemp = myCallingObject.innerHTML;
		strTemp = strTemp.replace(/<img src(.|\n)+?>/gi,"");
	
		strTemp = "<img src=\"" + aPath + "/DOWN.gif\"> " + strTemp;
	
		myCallingObject.innerHTML = strTemp;
	
	}
	
	function check_for_sorted(myCallingObject)
	{
		// If the column has an arrow then it is sorted
		var reImage;
		var result;
		var strTemp;
	
		strTemp = myCallingObject.innerHTML;
	
		// check if arrow is up or down
		reImage = new RegExp("<img src(.|\n)+?>","i");
		if (reImage.test(strTemp))
			result = true;
		else
			result = false;
	
		return result;
	}
	
	function TableSortByColumn(myTable, myColumn, myType, myCallingObject, myStepBack)
	{
		var mySource = document.getElementById(myTable);
		var myRows = mySource.rows.length;
		var myCols = mySource.rows[0].cells.length;
		var i;
		var j;
		currentCol = myColumn;
		var myArray = new Array(myRows);
		for (i=0; i < myRows; i++)
			{
			 myArray[i] = new Array(myCols);
			 for (j=0; j < myCols; j++)
				 {
				 if (mySource.rows[i].cells[j] != null)
					 myArray[i][j] = mySource.rows[i].cells[j].innerHTML;
				 else
					 myArray[i][j] = "";
				 }
			}
	
		if (check_for_sorted(myCallingObject))
			{
			switchImage(myCallingObject);
			myArray.reverse();
			}
		else
			{
			setImageDown(myCallingObject,myStepBack);
			switch (myType)
				{
				case "a":
						myArray.sort(CompareAlpha);
						break;
				case "d":
						myArray.sort(CompareDate);
						break;
				case "n":
						myArray.sort(CompareNumeric);
						break;
				case "m":
						myArray.sort(CompareMoney);
						break;
				default:
			myArray.sort(CompareAlpha);
			break;
				}
			}
	
		for (i=0; i < myRows; i++)
			{
			for (j=0; j < myCols; j++)
				{
							if (mySource.rows[i].cells[j] != null)
					mySource.rows[i].cells[j].innerHTML = myArray[i][j];
				}
			}
	}
	
	function OnlineUserRegistrationCheck(formobj){
		// Enter name of mandatory fields
		var fieldRequired = Array("firstname", "lastname", "street", "city", "state", "zip", "pin", "validatepin");
		// Enter field description to appear in the dialog box
		var fieldDescription = Array("First Name", "Last Name", "Street", "City", "State", "Zip", "PIN", "Re-Type PIN");
		// dialog message
		var alertMsg = "" + ":\n";
	
		var l_Msg = alertMsg.length;
	
		for (var i = 0; i < fieldRequired.length; i++){
			var obj = formobj.elements[fieldRequired[i]];
			if (obj){
				switch(obj.type){
				case "select-one":
					if (obj.selectedIndex == -1 || obj.options[obj.selectedIndex].text == ""){
						alertMsg += " - " + fieldDescription[i] + "\n";
					}
					break;
				case "select-multiple":
					if (obj.selectedIndex == -1){
						alertMsg += " - " + fieldDescription[i] + "\n";
					}
					break;
				case "text":
				case "textarea":
					if (obj.value == "" || obj.value == null){
						alertMsg += " - " + fieldDescription[i] + "\n";
					}
					break;
				default:
				}
				if (obj.type == undefined){
					var blnchecked = false;
					for (var j = 0; j < obj.length; j++){
						if (obj[j].checked){
							blnchecked = true;
						}
					}
					if (!blnchecked){
						alertMsg += " - " + fieldDescription[i] + "\n";
					}
				}
			}
		}
	
		if (alertMsg.length == l_Msg){
			if(formobj.pin.value != formobj.validatepin.value) {
							alert ("Los números PIN introducidos no coinciden.  Vuelva a introducir la información de PIN.");
				return false;
			}
			return true;
		}else{
			alert(alertMsg);
			return false;
		}
	}
	
	function OnlineUserActivationCheck(formobj){
		// Enter name of mandatory fields
		var fieldRequired = Array("user_id", "pin", "new_user_id");
		// Enter field description to appear in the dialog box
		var fieldDescription = Array("Temporary ID", "PIN", "New User ID");
		// dialog message
		var alertMsg = "Please complete the following required fields:\n";
	
		var l_Msg = alertMsg.length;
	
		for (var i = 0; i < fieldRequired.length; i++){
			var obj = formobj.elements[fieldRequired[i]];
			if (obj){
				switch(obj.type){
				case "select-one":
					if (obj.selectedIndex == -1 || obj.options[obj.selectedIndex].text == ""){
						alertMsg += " - " + fieldDescription[i] + "\n";
					}
					break;
				case "select-multiple":
					if (obj.selectedIndex == -1){
						alertMsg += " - " + fieldDescription[i] + "\n";
					}
					break;
				case "text":
				case "textarea":
					if (obj.value == "" || obj.value == null){
						alertMsg += " - " + fieldDescription[i] + "\n";
					}
					break;
				default:
				}
				if (obj.type == undefined){
					var blnchecked = false;
					for (var j = 0; j < obj.length; j++){
						if (obj[j].checked){
							blnchecked = true;
						}
					}
					if (!blnchecked){
						alertMsg += " - " + fieldDescription[i] + "\n";
					}
				}
			}
		}
	
		if (alertMsg.length == l_Msg){
			return true;
		}else{
			alert(alertMsg);
			return false;
		}
	}
	
	function showTab(tabId)
	{
		var myTabs = new Array();
		var myCount;
		var myObject;
		var strTab;
	
		myTabs[0] = "account_summary";
		myTabs[1] = "account_charges";
		myTabs[2] = "account_suspensions";
		myTabs[3] = "account_holds";
		myTabs[4] = "account_bills";
		myTabs[5] = "account_bookings";
		myTabs[6] = "account_reservations";
		myTabs[7] = "email_and_pin";
	
		if (tabId == "")
			strTab = myTabs[0];
		else
			strTab = tabId;
	
		// purely defensive - found a way to reach this state
		// when testing without logging in to view my account
		myObject = document.getElementById(strTab);
		if (myObject == null)
			strTab = myTabs[0];
	
		sendCurrentTab(strTab);
	
		for (myCount = 0; myCount < myTabs.length; myCount++)
			{
			myObject = document.getElementById(myTabs[myCount]);
			if (myObject != null)
				{
				myObject.style.display='none';
				}
			myObject = document.getElementById(myTabs[myCount] + '_tab');
			if (myObject != null)
				{
				myObject.className='tabOff';
				}
			}
	
		myObject = document.getElementById(strTab);
		if (myObject != null)
			myObject.style.display='block';
		myObject = document.getElementById(strTab + '_tab');
		if (myObject != null)
			myObject.className='tab';
	}
	
	function selectAll(inForm,inBox) 
	{
		var checkboxes = document.getElementById(inForm).length;
	
		if (document.getElementById(inBox).checked == true)
						{
			for (i=0; i < checkboxes; i++) 
				{
				if (document.getElementById(inForm)[i].onclick == null &&
			document.getElementById(inForm)[i].type == "checkbox")
					document.getElementById(inForm)[i].checked = true;
				}
			}
					else 
			{
			for (i=0; i < checkboxes; i++)
				{
				if (document.getElementById(inForm)[i].onclick == null && 
			document.getElementById(inForm)[i].type == "checkbox")
					document.getElementById(inForm)[i].checked = false;
				}
			}
	}
	
	function NewCalHold(pCtrl,pFormat,pShowTime,pTimeMode,inCheckbox)
	{
		var myCheckbox;
	
		myCheckbox = document.getElementById(inCheckbox);
		
		if (myCheckbox.checked != true)
			NewCal(pCtrl,pFormat,pShowTime,pTimeMode);
	}
	
	function cancelSelected()
	{
		var myCheckbox;
		var mySubmit;
	
		myCheckbox = document.getElementById("cancelselected");
		mySubmit = document.getElementById("submitholdsbutton");
		mySelect = document.getElementById("pickup_library");
		myExpiration = document.getElementById("hold_expiration_date");
	
		if (myCheckbox != null && myCheckbox.checked == true)
			{
			if (mySubmit != null)
				mySubmit.value = 'Cancelar reservas seleccionadas';
			if (mySelect != null)
				mySelect.disabled = true;
			if (myExpiration != null)
				myExpiration.disabled = true;
			}
		else
			{
			if (mySubmit != null)
				mySubmit.value = 'Editar reservas seleccionadas';
			if (mySelect != null)
				mySelect.disabled = false;
			if (myExpiration != null)
				myExpiration.disabled = false;
			}
	}
	
	function processholdform()
	{
		var myCheckbox;
		var myForm;
		var checkboxes;
		var conirmeditall;
		var count;
		var editall;
		var strWork;
		var strID;
		var pieces;
		var sometoedit;
		var nFORM;
		var nField;
		var myHoldExpiration;
		var myPickupLibrary;
	
		myCheckbox = document.getElementById("cancelselected");
	
		if (myCheckbox.checked == true)
			{
			myForm = document.getElementById("holds_list");
			if (myForm != null)
				{
				if (someChecked("holds_list"))
					{
					editall = allChecked("holds_list");
					if (editall)
						confirmeditall = confirm("Se están cambiando todas las reservas. ¿Continuar?");
	
					if (!editall || (editall && confirmeditall))
						{
						myForm.submit();
			}
					}
				else
					{
					window.alert("Por favor, revise las reservas que desea cancelar");
					}
				}
			}
		else
			{
			// The edit portion 
			myForm = document.getElementById("holds_list");
			if (myForm != null)
				{
				sometoedit = someChecked("holds_list");
				if (sometoedit)
					{
					editall = allChecked("holds_list");
					if (editall)
						confirmeditall = confirm("Se están cambiando todas las reservas. ¿Continuar?");
	
					if (!editall || (editall && confirmeditall))
						{
						myHoldExpiration = document.getElementById("hold_expiration_date").value;
						myPickupLibrary = document.getElementById("pickup_library").value;
									nFORM=document.createElement('form');
								 nFORM.action='/uhtbin/cgisirsi/?ps=YPpuGvHh6g/x/165390243/136';
						nFORM.target="_self";
						nFORM.method="post";
							nFORM.name="EditHolds";
						checkboxes = myForm.length;
						for (count = 0; count < checkboxes; count++)
							{
							if (myForm[count].id.indexOf("HLD") != -1)
								{
					if (myForm[count].checked == true)
						{
						strWork = myForm[count].id;
						pieces = strWork.split("^");
						strID = pieces[0] + "^" + pieces[5];
						strID = strID + "^" + pieces[3] + "^" + pieces[2];
		
						nField=document.createElement('input');
									nField.name=strID;
									nField.id=strID;
									nField.value='on';
									nField.type='hidden';
	
									nFORM.appendChild(nField);
						}
											}
				}
						nField=document.createElement('input');
						nField.name='hold_expiration_date';
						nField.id='hold_expiration_date';
						nField.value=myHoldExpiration;
						nField.type='hidden';
						nFORM.appendChild(nField);
						nField=document.createElement('input');
						nField.name='pickup_library';
						nField.id='pickup_library';
						nField.value=myPickupLibrary;
						nField.type='hidden';
						nFORM.appendChild(nField);
						document.body.appendChild(nFORM);
						nFORM.submit();
			}
					}
				else
					{
					window.alert('Revise las reservas que se desea editar');
					}
				}
			}
	}
	
	function processSuspend()
	{
		var myCheckbox;
		var myStartDate;
		var myEndDate;
		var myButton;
	
		myCheckbox = document.getElementById("activate");
		myStartDate = document.getElementById("suspend_start_date");
		myEndDate = document.getElementById("suspend_end_date");
		myButton = document.getElementById("submitactivatebutton");
	
		if (myCheckbox != null && myCheckbox.checked)
			{
			if (myStartDate != null)
				{
				myStartDate.disabled = true; 
				myStartDate.value = 'NEVER';
				}
			if (myEndDate != null)
				{
				myEndDate.disabled = true; 
				myEndDate.value = 'NEVER';
				} 
			if (myButton != null)
				myButton.value = 'Activar seleccionadas';
			}
		else
			{
			if (myStartDate != null)
				{
				myStartDate.disabled = false; 
				myStartDate.value = "TODAY";
				}
			if (myEndDate != null)
				{
				myEndDate.disabled = false; 
				myEndDate.value = 'NEVER';
				} 
			if (myButton != null)
				myButton.value = 'Suspender seleccionadas';
			}
	}
	
	function processactivateform()
	{
		var myCheckbox;
		var myForm;
		var checkboxes;
		var count;
		var confirmeditall;
		var editall;
		var strWork;
		var strID;
		var pieces;
		var sometoedit;
		var nFORM;
		var nField;
		var myStartDate;
		var myEndDate;
	
		// The edit portion 
		myForm = document.getElementById("holds_list");
		if (myForm != null)
			{
			sometoedit = someChecked("holds_list");
			if (sometoedit)
				{
				editall = allChecked("holds_list");
				if (editall)
					confirmeditall = confirm("Se están cambiando todas las reservas. ¿Continuar?");
	
				 if (!editall || (editall && confirmeditall))
				 { 
	
					myStartDate = document.getElementById("suspend_start_date").value;
					myEndDate = document.getElementById("suspend_end_date").value;
								nFORM=document.createElement('form');
							 nFORM.action='/uhtbin/cgisirsi/?ps=nohoyKuCiA/x/165390243/136';
					nFORM.target="_self";
					nFORM.method="post";
						nFORM.name="SuspendHolds";
					checkboxes = myForm.length;
					for (count = 0; count < checkboxes; count++)
						{
						if (myForm[count].id.indexOf("HLD") != -1)
							{
							if (myForm[count].checked == true)
					{
					strWork = myForm[count].id;
					pieces = strWork.split("^");
					strID = pieces[0] + "^" + pieces[5];
					strID = strID + "^" + pieces[3] + "^" + pieces[2];
	
					nField=document.createElement('input');
								nField.name=strID;
								nField.id=strID;
								nField.value='on';
								nField.type='hidden';
	
								nFORM.appendChild(nField);
					}
										}
						}
					nField=document.createElement('input');
					nField.name='suspend_start_date';
					nField.id='suspend_end_date';
					nField.value=myStartDate;
					nField.type='hidden';
					nFORM.appendChild(nField);
					nField=document.createElement('input');
					nField.name='suspend_end_date';
					nField.id='suspend_end_date';
					nField.value=myEndDate;
					nField.type='hidden';
					nFORM.appendChild(nField);
					document.body.appendChild(nFORM);
					nFORM.submit();
					}
				}
			else
				{
				window.alert('Revise las reservas que desee activar o suspender');
				}
			}
	}
	
	function sendCurrentTab(inTab)
	{
		var myImage;
		var aImage;
	
		aImage = document.getElementById("settab");
	
		myImage = new Image();
		myImage.src = '/uhtbin/cgisirsi/?ps=x71no5MnoG/x/165390243/148/' + inTab;
		aImage.src=myImage.src;
		myImage = new Image();
		myImage.src = '/WebCat_Images/Castellano/Other/Miscil/clear.gif';
		aImage.src=myImage.src;
	}
	
	function verifyAndSubmit(inForm)
	{
		if (!someChecked(inForm))
			ask_to_select(inForm);
		else
			{
			if (allChecked(inForm))
				{
				if (ask_for_confirmation(inForm))
					{
					submitForm(inForm);
					}
				}
				else
					{
					submitForm(inForm);
					}
			}
	}
	
	function allChecked(inForm)
	{
		var allselected = false;
	
		var myForm;
	
		myForm = document.getElementById(inForm);
		if (myForm != null)
			{
			allselected = true;
			checkboxes = myForm.length;
			for (count = 0; count < checkboxes; count++)
				if (myForm[count].type == 'checkbox')
					if (myForm[count].onclick == null)
						if (myForm[count].checked == false)
				allselected = false;
			}
	
		return allselected;
	}
	
	function someChecked(inForm)
	{
		var somechecked = false;
		var myForm;
	
		myForm = document.getElementById(inForm);
		if (myForm != null)
			{
			checkboxes = myForm.length;
			for (count = 0; count < checkboxes; count++)
				if (myForm[count].type == 'checkbox')
					if (myForm[count].onclick == null)
						if (myForm[count].checked == true)
				somechecked = true;
			}
	
		return somechecked;
	}
	
	function ask_to_select(inForm)
	{
		var strMessage;
	
		strMessage = "No se ha seleccionado nada.";
	
		if (inForm == "renewitems")
			strMessage = "No se seleccionaron documentos para renovar";
		if (inForm == "rsvns_list")
			strMessage = "Compruebe las reservas que desee cancelar";
	
		window.alert(strMessage);
	}
	
	function ask_for_confirmation(inForm)
	{
		var strMessage;
	
		strMessage = "Se han seleccionado todos. ¿Continuar?";
	
		if (inForm == "renewitems")
			strMessage = "Se están cambiando todos los préstamos. ¿Continuar?";
		if (inForm == "avail_list")
			strMessage = "Se está a punto de cancelar todas las reservas listas para recoger. ¿Continuar?";
	
		return confirm(strMessage);
	}
	
	function submitForm(inForm)
	{
		var myForm;
	
		myForm = document.getElementById(inForm);
	
		if (myForm != null)
			myForm.submit();
	}
	
	</script>
	
	
		
	<script language="JavaScript" type="text/javascript">
		 var currentPanel;
		 function showPanel(panelNum) {
				//hide visible panel, show selected panel, 
				//set tab
				if (currentPanel != null) {
					 hidePanel();
				}
				document.getElementById 
					 ('panel'+panelNum).style.display = 'block';
					 currentPanel = panelNum;
					 setState(panelNum);
		 }
		 function hidePanel() {
				//hide visible panel, unhilite tab
				document.getElementById
					('panel'+currentPanel).style.display = 'none';
				document.getElementById
					('tab'+currentPanel).style.backgroundColor = 
					'#006699';
				document.getElementById
					('tab'+currentPanel).style.color = '#FFFFFF';
		 }
		 function setState(tabNum) {
				if (tabNum==currentPanel) {
					 document.getElementById 
						 ('tab'+tabNum).style.backgroundColor = 
						 '#FFFFFF';
					 document.getElementById
						 ('tab'+tabNum).style.color = '#006699';
				}
				else {
					 document.getElementById
						 ('tab'+tabNum).style.backgroundColor = 
						 '#006699';
					 document.getElementById
						 ('tab'+tabNum).style.color = '#FFFFFF';
				}
		 }
		 function hover(tab) {
				tab.style.backgroundColor = '#EEEEEE';
				tab.style.color = '#006699';
		 }
	</script>
		
	
	<style type="text/css">
	
	a:link, a:active {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 11px;
		font-weight: normal;
		text-decoration: none;
		color: #006699;
	}
	
	a:visited {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 11px;
		font-weight: normal;
		text-decoration: none;
		color: #006699;
	}
	
	a:hover {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 11px;
		font-weight: normal;
		text-decoration: underline;
		color: #FF0000;
		background-color: #FFFFCC;
	}
	
	body {
		margin:-10px 0px 0px -10px;
		background-color: #FFFFFF;
		color: #000000;	
	}
	
	html body {
		margin: 10px 10px 10px 10px;
		background-color: #FFFFFF;
		color: #000000;	
	}
	
	p, td {
		font-family: Verdana, Helvetica, Arial, sans-serif;
	}
	
	th {
		font-family: Verdana, Helvetica, Arial, sans-serif;
		text-align: left;
		vertical-align: top;
	}
	
	label {
		font-family: Verdana, Helvetica, Arial, sans-serif;
		font-weight: bold;
	}
	
	legend {
		font-family: Verdana, Helvetica, Arial, sans-serif;
		font-weight: bold;
	}
	
	fieldset {
		border-style: none;
		border-width: 0px;
	}
	
	form {
		margin: 0px 0px 0px 0px;
	}
	
	ul {
		margin-left: 0px;
	}
	
	.bibinfo {
		font-family: Verdana, Helvetica, Arial, sans-serif;
		font-size: 12px;
		background-color: #FFFFFF;
		color: #000000;
		border-width: 0px;
		border-style: none;
		margin: 5px 5px 5px 5px;
		text-align: left;
		width: 100%;
	}
	
	.bibinfo2 {
		font-family: Verdana, Helvetica, Arial, sans-serif;
		font-size: 12px;
		background-color: #FFFFFF;
		color: #000000;
		margin: 10px 30px 10px 30px;
	}
	
	.summary {
		background-color: #FFFFFF;
		font-family: Verdana, Helvetica, Arial, sans-serif;
		font-size: 11px;
		color: #000000;
		border-width: 1px;
		border-style: solid;
		padding: 5px 5px 5px 5px;
		margin: 10px 5px 5px 10px;
	}
	
	.rootbarcell {
		font-family: Verdana, Helvetica, Arial, sans-serif;
		text-align: center;
		color: #FFFFFF;
		background-color: #666666;
		letter-spacing: 0px;
		margin: 5px 5px 5px 5px;
	}
	
	 /* Use these rootbar declaration for CSS2 browsers */
	
	a:link.blastoff, a:visited.blastoff, a:active.blastoff {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 12px;
		font-weight: bold; 
		color: #FFFF99;
		background-color: #666666;
		text-decoration: none;
		white-space: nowrap;
		margin: 0px 7px 0px 7px;
	}
	
	a:hover.blastoff {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 12px;
		font-weight: bold; 
		color: #FFFFFF;
		background-color: #666666;
		text-decoration: underline;
		white-space: nowrap;
		margin: 0px 7px 0px 7px;
	}
	a:link.rootbar, a:visited.rootbar, a:active.rootbar {
		font-family: Verdana, Helvetica, Arial, sans-serif;
		font-size: 12px;
		font-weight: normal;
		color: #FFFFFF;
		background-color: #666666;
		text-decoration: none;
		white-space: nowrap;
		margin: 0px 7px 0px 7px;
	}
	
	a:hover.rootbar {
		font-family: Verdana, Helvetica, Arial, sans-serif;
		font-size: 12px;
		font-weight: normal;
		color: #FFFF99;
		background-color: #666666;
		text-decoration: underline;
		white-space: nowrap;
		margin: 0px 7px 0px 7px;
	}
	
	
	
	.accountstyle {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 12px;
		color: #000000;
		vertical-align: top;
	}
	
	.defaultstyle {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 12px;
		background-color: #FFFFFF;
		color: #000000;
		vertical-align: top;
	}
	th.defaultstyle {
		white-space: nowrap;
		text-align: right;
	}
	
	
	.enrichheader, .enrichheader a {
		background-color: #FFFFFF; 
		color: #996600; 
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 12px;
		font-weight: bold;
		letter-spacing: 2px;
		padding: 5px 0px 0px 0px;
	}
	
	.enrichsubheader {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 12px;
		font-weight: bold;
		letter-spacing: 2px;
	}
	.enrichcontent {
		background-color: #FFFFFF; 
		color: #000000; 
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 11px;
		vertical-align: top;
		padding: 0px 0px 5px 5px;
	} 
	
	.enrichmentservices {
		background-color: #FFFFFF;
		font-family: Verdana, Helvetica, Arial, sans-serif;
		font-size: 10px;
		color: #000000;
		border-width: 1px;
		border-style: solid;
		text-align: left;
	}
	
	.enrichtagline {
		font-family: Verdana, Helvetica, Arial, sans-serif;
		font-size: 10px;
		font-weight: normal;
		background-color: #FFFFFF;
		color: #888888;
	}
	
	.footer {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 10px;
		font-weight: normal; 
	}
	
	.gatewaystyle, .gatewaystyle a:link, .gatewaystyle a:visited, .gatewaystyle a:active, .gatewaystyle a:hover {
		background-color: #003366;
		color: #FFFFFF;
		margin: 0px 0px 0px 0px;
	}
	
	.header {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 11px;
		font-weight: bold;
		letter-spacing: 2px; 
		background-color: #006699;
		color: #FFFFFF;
	}
	
	div.header {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 11px;
		font-weight: bold;
		letter-spacing: 2px; 
		background-color: #006699;
		color: #FFFFFF;
		padding: 3px 3px 3px 3px;
	}
	
	.holdingsheader {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 11px;
		font-weight: bold;
		background-color: #FFFFFF;
		color: #006699;
	}
	
	.holdingslist {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 10px;
		background-color: #FFFFFF;
		color: #000000;
	}
	
	th.holdingslist {
		white-space: nowrap;
		text-align: right;
		vertical-align: top;
	}
	
	.indented {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 12px;
		background-color: #FFFFFF;
		color: #000000;
		margin-left: 10px;
		vertical-align: top;
	}
	
	.itemlisting, label.itemlisting {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 11px;
		background-color: #FFFFFF;
		color: #000000;
		vertical-align: top;
		font-weight: normal;
	}
	
	.itemlisting2, label.itemlisting2 {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 11px;
		background-color: #EFEFEF;
		color: #000000;
		vertical-align: top;
		font-weight: normal;
	}
	
	input.itemdetails {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 11px;
		background-color: #003366;
		color: #FFFFFF;
		width: 75px;
		margin: 5px 0px 5px 0px;
		display: block;
	}
	
	input.itemdetails2 {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 11px;
		background-color: #666666;
		color: #FFFFFF;
		width: 75px;
		margin: 5px 0px 5px 0px;
		display: block;
	}
	
	td.itemservices {
		background-color: #FFFFFF;
		font-family: Verdana, Helvetica, Arial, sans-serif;
		font-size: 11px;
		color: #000000;
	}
	
	div.itemservices {
		background-color: #FFFFFF;
		font-family: Verdana, Helvetica, Arial, sans-serif;
		font-size: 11px;
		color: #000000;
		text-align: left;
		border-width: 1px;
		border-style: solid;
		padding: 7px 7px 7px 7px;
		margin: 0px 0px 0px 0px;
	}
	
	div.itemservices a:link, div.itemservices a:visited, div.itemservices a:active {
		display: block;
		margin: 3px 0px 3px 0px;
	}
	
	div.itemservices a:hover {
		background-color: #FFFFCC;
		color: #FF0000;
		display: block;
		margin: 3px 0px 3px 0px;
	}
	
	.langicon {
		font-family: Verdana, Helvetica, Arial, sans-serif;
		font-size: 11px;
		text-align: center;
		background-color: #003366;
		letter-spacing: 0px; 
		padding: 0px 0px 3px 0px;
	}
	
	a.holdicon:link { 
		color: #FFFFFF;
		border-style: outset;
		border-width: thin; 
		border-color: #EEEEEE;;
		background-color: #003366;
		text-decoration: none;
		text-align: center;
		width: 73px;
		display: block;
		padding: 1px 1px 1px 1px;
		margin: 0px 0px 0px 0px;
	}
	
	a.holdicon:hover {
		color: #FFFFFF;
		border-style: outset;
		border-width: thin; 
		border-color: #EEEEEE;;
		background-color: #003366;
		text-decoration: none;
		text-align: center;
		width: 73px;
		display: block;
		padding: 1px 1px 1px 1px;
		margin: 0px 0px 0px 0px;
	}
	
	div.options {
		background-color: #FFFFFF;
		font-family: Verdana, Helvetica, Arial, sans-serif;
		font-size: 11px;
		color: #000000;
		border-width: 1px;
		border-style: solid;
		padding: 5px 5px 5px 5px;
		margin: 10px 5px 5px 10px;
	}
	
	.overdue, .error {
		color: #CC0000;
	}
	
	.pagecontainer {
		background-color: #FFFFFF;
		font-family: Verdana, Helvetica, Arial, sans-serif;
		font-size: 12px;
		color: #000000;
		border-width: 1px;
		border-style: solid;
	}
	
	.pagecontainer3pg {
		background-color: #FFFFFF;
		font-family: Verdana, Helvetica, Arial, sans-serif;
		font-size: 12px;
		color: #000000;
		border-width: 1px;
		border-style: solid;
		
	}
	
	.rsvholdings {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 10px;
		background-color: #FFFFCC;
		color: #000000;
	}
	
	.searchheader {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 12px;
		font-weight: bold;
		letter-spacing: 2px; 
		background-color: #006699;
		color: #FFFFFF;
		padding: 3px 3px 3px 3px;
		width: 100%;
	}
	
	.searchcontent {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 12px;
		background-color: #EEEEEE;
		color: #000000;
		padding: 3px 3px 3px 3px;
		vertical-align: middle;
		white-space: nowrap;
	}
	
	table.searchcontent {
		width: 99%;
	}
	
	th.searchcontent {
		text-align: right;
		width: 30%;
	}
	
	
	.searchservices {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 12px;
		background-color: #EEEEEE;
		color: #000000;
		border-width: 1px;
		border-style: solid;
	}
	
	input.searchbutton {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 11px;
		font-weight: bold;
		background-color: #003366;
		color: #FFFFFF;
		vertical-align: middle;
		margin: 5px;
	}
	
	a:link.searchlinks, a:active.searchlinks, a:visited.searchlinks {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 12px;
		font-weight: bold;
		text-decoration: none;
		background-color: #EEEEEE;
		color: #006699;
	}
	
	a:hover.searchlinks {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 12px;
		font-weight: bold;
		text-decoration: underline;
		background-color: #EEEEEE;
		color: #CC0000;
	}
	
	.subheader {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 12px;
		background-color: #EEEEEE;
		color: #000000;
		margin-left: 2px;
	}
	
	.sortsubheader {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 12px;
		background-color: #EEEEEE;
		color: #000000;
		margin-left: 2px;
		cursor: pointer;
		text-decoration: underline;
	}
	
	.searchsum {
		color: #000000;
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 11px;
		text-align: center;
		background-color: #FFFFFF;
	}
	
	.small {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 10px;
		font-weight: normal; 
	}
	
	.titlebar {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 14px;
		font-weight: bold;
		letter-spacing: 3px;
		background-color: #006699;
		color: #FFFFFF;
		vertical-align: top;
		padding: 3px;
	}
	
	.vreference {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 10px;
		text-decoration: none;
		font-weight: normal;
		letter-spacing: 0px;
		background-color: #006699;
		color: #FFFFFF;
	}
	
	.vreference input {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 10px;
		text-decoration: none;
		font-weight: normal;
		letter-spacing: 0px;
		background-color: #FFFFFF;
		color: #006699;
		margin: 3px 3px 3px 3px;
	}
	
	.vreference textarea {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 10px;
		text-decoration: none;
		font-weight: normal;
		letter-spacing: 0px;
		background-color: #FFFFFF;
		color: #006699;
		width: 125px;
		height: 50px;
		margin: 3px 3px 3px 3px;
	}
	
	.unformatted {
		font-family: "Courier New", Courier, monospace; 
		font-size: 12px;
		font-weight: normal; 
		vertical-align: top;
	}
	
	.viewmarcheader, .viewmarcheader a {
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 12px;
		font-weight: bold;
		letter-spacing: 2px;
		background-color: #FFFFFF;
		color: #996600;
	}
	
	.tab {
		border-top:1px solid #cccccc;
		border-right:1px solid #a9a9a9;
		margin-right:5px;
		border-left:1px solid #cccccc;
		background-color:#fefef2;
		padding:1px 4px 1px 4px;
		font-size:10pt;
	}
	
	.tabOff {
		color:#ffffff;
		background-color:#0c0575;
		background-image:url(/WebCat_Images/Castellano/Special/Link/button.png);
		background-position:top left;
		background-repeat:repeat-x;
		border-top:2px solid #050568;
		border-right:2px solid #050568;
		border-left:2px solid #050568;
		margin-right:10px;
		padding:1px 4px 1px 4px;
		font-size:10pt;
	}
	
	a.tabOff, a.tabOff:visited, a.tabOff:hover {
		color:#ffffff;
		background-color:#0c0575;
	}
	
	.panelholder {
		background-color:#fefef2;
		border-top:1px solid #cccccc;
		border-right:1px solid #a9a9a9;
		border-bottom:1px solid #a9a9a9;
		border-left:1px solid #cccccc;
		padding:10px;
		margin:0px;
	}
	
	.viewmarctags {
		vertical-align: top;
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 10px;
		background-color: #FFFFFF;
		color: #000000;
	}
	
	th.viewmarctags {
		white-space: nowrap;
		text-align: right;
		vertical-align: top;
	}
	
	.virtualreference {
		border-style: none;
		border-width: 0px;
		padding: 1px 5px 1px 5px;
	}
	
	</style>
		
	<style type="text/css">
	
	.pagecontainer {
		color: #000000;
		background-color: #FFFFFF;
		padding: 0px 0px 10px 0px;
		border-width: 1px;
		border-style: solid;
		width: 100%;
		position: relative;
	}
	
	.contentholder {
		padding: 10px 10px 10px 10px;
		position: relative;
	}
	
	.tabholder {
		padding: 0px 0px 0px 0px;
		z-index: 2;
	}
	
	.tab {
		border-style: outset;
		border-bottom-style: none;
		border-width: 2px;
		border-color: #999999;
		line-height: 150%;
		text-align: center;
		padding: 4px;
		margin-right: 5px;
		margin-left: 5px;
		cursor: pointer;
		cursor: hand;
		font-family: Verdana, Helvetica, Arial, sans-serif; 
		font-size: 10px;
		font-weight: bold;
		background-color: #006699;
		color: #FFFFFF;				 
	}
	
	.panelholder {
		position: relative;
		top: -2px;
		z-index: 1;
		visibility: visible;
		display: block;
		color: #000000;
		background-color: #FFFFFF;
	}
	
	.panel {
		position: relative;
		color: #000000;
		background-color: #FFFFFF;
		border: 2px;
		border-color: #999999;
		border-style: outset;
		top: 0;
		left: 0;
		padding: 10px 10px 10px 10px;
		display: none;
	}
	
	.contentholder {
		position: relative;
		padding: 10px;
	}
	
	</style>
		
	
	</head>
	<!-- if copies=0 or no holdings allowed, default tab to Catalog Record  -->
	<!-- Start the body of the document.  WARNING:  No comments are allowed inside of the body element's definition. - assign CSS Class of 'body_style' to tag -  If this is a download search results state (14, 62), then load the results in a new browser window to facilitate printing. -  If this is an Archive image view state (911), then open a new window to display the image in new window. -  To help prevent premature selection of a toolbar button (i.e., before the new toolbar is loaded), clear it when the page is unloaded. -->
	<body onload=" showPanel(1);">
	
	<noscript>
	Your browser does not support JavaScript and this application utilizes JavaScript to build content and provide links to additional information. You should either enable JavaScript in your browser settings or use a browser that supports JavaScript in order to take full advantage of this application.
	</noscript>
	<!--  Copyright (c) 2000 - 2008, SirsiDynix - Unicorn Item View Page; State #5 -->
	<!--  Copyright (c) 1996 - 2008, SirsiDynix. Form for starting a new session in a new window. -->
	
	<!-- By setting the "document.new_session.action" property to the URL for logging into a new session at the particular  page you want, a new window will be opened and a new WebCat session will be started automatically. Remember that many WebCat states are dependent on previous states, so only certain "cgi types" can be opened.
	
	Also, by setting the "document.new_session.new_gateway_db.value" property to a gateway database name, the new session will use that gateway instead of the user's default gateway. Note that the use of Javascript is required to submit this form. -->
	
	<form name="new_session" method="post" action="/uhtbin/cgisirsi/?ps=PqeaQB5NdA/x/0/57/49" target="new_session">
		<input type="hidden" name="user_id" value="WEBSERVER">
		<input type="hidden" name="password" value="">
		<input type="hidden" name="new_gateway_db" value="">
	</form>
	
	
	<!--  Copyright (c) 2000 - 2008, SirsiDynix - Puts the top-of-page information common to all pages. -->
	<a href="#skipnav"><img src="/WebCat_Images/Castellano/Other/Miscil/clear.gif" height="1" width="1" border="0" alt="Ignorar navegación" title="Ignorar navegación"></a>  <a name="top"></a>
	<div class="pagecontainer"> <!-- Controls Page Border -->
	
	
	<table border="0" cellpadding="3" cellspacing="0" width="100%"> <!-- title bar -->
	 <tbody><tr>
		<td class="titlebar" align="left">
				<img border="0" src="/WebCat_Images/Castellano/Other/Miscil/LIBLOGO.gif" alt="" title="">
		</td>
	
		<td class="titlebar" align="center">
			<!-- Print the gateway envn title if not blank -->
				<!-- icon was printed -->
				Biblioteca<br>Universidad de Alicante<br><br>
		 <br>
			<!-- present language choices -->
			 <div align="center" class="footer">
	<!-- Add the Language options -->
		<!-- Suppress an option for the current language -->
			<a href="/uhtbin/cgisirsi/?ps=W9uBikknCU/x/165390243/111/INGLES" title="English" target="_top"><img src="/WebCat_Images/Castellano/Other/Miscil/INGLES.gif" border="0" class="langicon" alt="&nbsp;English&nbsp;" title="English" align="center"></a>
		<!-- Suppress an option for the current language -->
			<a href="/uhtbin/cgisirsi/?ps=jYPjuQITLq/x/165390243/111/CATALAN" title="Valencià" target="_top"><img src="/WebCat_Images/Castellano/Other/Miscil/CATALAN.gif" border="0" class="langicon" alt="&nbsp;Valencià&nbsp;" title="Valencià" align="center"></a>
		<!-- Suppress an option for the current language -->
			 </div>
		</td>
			<!-- no VIRTUAL_REF form -->
			 <td valign="top" class="header">
			 <form name="loginform" method="POST" action="/uhtbin/cgisirsi/?ps=lTPuyLCSV0/x/165390243/303">
	<!--  Copyright (c) 2004 - 2008, SirsiDynix - myProfile login or view myFavorites -->
	<!--  Copyright (c) 1998 - 2003, Sirsi Corporation - Sets the default values for USER_ID, ALT_ID, and PIN prompts. - The USER_ID, ALT_ID, and PIN page variables will be returned. -->
	
	<!-- If the user has not logged in, first try to default to the ID based on the IP address - the $UO and $Uf will be set.  If that fails, then default to the IDs in the config file. If the user has already logged in, default to the logged in user's IDs, unless the user is a shared login. -->
	
	
	
		<table class="header" border="0" cellspacing="0" cellpadding="2">
		 <tbody><tr>
						 <!-- only user ID is used if both on -->
			<td align="right" valign="middle"><label for="user_id">ID de usuario:</label></td>
			<td align="left" valign="middle"><input type="text" name="user_id" id="user_id" size="8" maxlength="20" value=""></td>
		 
		 </tr>
	
			
		 <tr>
			<td align="right" valign="middle"><label for="password">NIP:</label></td>
			<td align="left" valign="middle"><input type="password" name="password" id="password" size="8" maxlength="20" value=""></td>  
		 </tr>
		 
		 <tr>
			<td colspan="2" align="center"><input type="submit" value="Acceso a perfil" class="searchbutton"></td>
		 </tr>
		 <tr>
			
		 </tr>
		</tbody></table>
	
	
			 </form>
			 </td>
			 <!-- login form-->
		<td valign="top" class="defaultstyle"><!-- container cell -->
	<!--  Copyright (c) 2000 - 2006, SirsiDynix - Announcements/Activity - This page file is processed by a  SIRSI_Command for an Si response. -->
	 <table border="0" cellspacing="0" cellpadding="0">
		<tbody><tr>
		 <td class="enrichheader">Información de la biblioteca</td>
		</tr>
		<tr>
		 <td class="enrichcontent">
		
				 <a href="javascript:open_win('http://biblioteca.ua.es/es/encuentra-informacion/bibliografia-recomendada.html')">Bibliografía recomendada</a><br>
			<!-- counter test -->
		
				 <a href="/uhtbin/cgisirsi/?ps=vIXFvUJk3O/x/165390243/1/60/X">Nuevas adquisiciones</a><br>
			<!-- counter test -->
		
				 <a href="javascript:open_win('http://biblioteca.ua.es/es/estudia-y-aprende/autoaprendizaje.html')">Tutoriales</a><br>
			<!-- counter test -->
		
				 <a href="javascript:open_win('http://biblioteca.ua.es/es/utiliza-la-biblioteca/la-biblioteca-desde-casa.html')">Acceso a los recursos electrónicos desde fuera de la UA</a><br>
			<!-- counter test -->
		 </td>
		</tr>
	 </tbody></table>
	
		</td> <!-- container cell -->	
	 </tr>
	</tbody></table>
	<table border="0" cellpadding="3" cellspacing="0" width="100%"> <!-- title bar -->
	 <tbody><tr>
		<td class="rootbarcell">
	<!--  Copyright (c) 1996 - 2008, SirsiDynix - Gateway Root Bar. -->
			<!-- display text with CSS instead -->
						<a href="/uhtbin/cgisirsi/?ps=BjCxlHWyJv/x/165390243/38/1/X/BLASTOFF" class="blastoff">
				 Catálogo de la biblioteca</a>
						<a href="/uhtbin/cgisirsi/?ps=FRnzKMKHFS/x/165390243/1/2829/X/BLASTOFF" class="rootbar">
				 Colección digital UA</a>
						<a href="/uhtbin/cgisirsi/?ps=44xiXlyAOq/x/165390243/1/2830/X/BLASTOFF" class="rootbar">
				 Colecciones especiales</a>
						<a href="/uhtbin/cgisirsi/?ps=fL5qN10haQ/x/165390243/1/29/X/BLASTOFF" class="rootbar">
				 Recursos electrónicos</a>
						<a href="/uhtbin/cgisirsi/?ps=4LI52gjSO3/x/165390243/1/121/X/BLASTOFF" class="rootbar">
				 Servicios al usuario</a>
						<a href="/uhtbin/cgisirsi/?ps=BF3Ubx4CTR/x/165390243/63/170/X/BLASTOFF" class="rootbar">
				 Solicitud</a>
	
	
	
		</td>
	 </tr>
	</tbody></table>
	<form name="item_view" method="post" action="/uhtbin/cgisirsi/?ps=Tp79KuTPAj/x/165390243/13">
	<!--  Copyright (c) 2000 - 2008, SirsiDynix - Buttons for Item View page, state #5. -->
	<table border="0" cellpadding="0" cellspacing="0" width="100%" class="gatewaystyle">
	 <tbody><tr>
		<td class="gatewaystyle">
	
		 <!-- Go back button -->
		 <a href="/uhtbin/cgisirsi/?ps=BzuRaGlKvK/x/165390243/2/18" title="VOLVER"><img src="/WebCat_Images/Castellano/Buttons/Link/GOBACK.gif" border="0" alt="VOLVER" title="VOLVER"></a>
	
		<!-- Help button -->
		<script language="JavaScript" type="text/javascript">
			put_help_button('Castellano','AYUDA','full_details');
		</script><a href="#" onclick="javascript:open_help_win('/iBistro_helps/User/Castellano/index.htm?context=elibrary&amp;topic=full_details')" alt="AYUDA" title="AYUDA"><img src="/WebCat_Images/Castellano/Buttons/Link/HELP.gif" border="0" alt="AYUDA" title="AYUDA"></a>
	
		
		<a href="/uhtbin/cgisirsi/?ps=Yar0VrgXhs/x/165390243/49" title="NUEVA BÚSQUEDA"><img src="/WebCat_Images/Castellano/Buttons/Link/NSEARCH.gif" border="0" alt="NUEVA BÚSQUEDA" title="NUEVA BÚSQUEDA"></a>
	
	<!-- Backward button -->
		<img src="/WebCat_Images/Castellano/Buttons/Link/UNBACKWARD.gif" border="0" alt="">
	
	<!-- Forward button -->
		<img src="/WebCat_Images/Castellano/Buttons/Link/UNFORWARD.gif" border="0" alt="">
	
	<!-- Cross Reference button -->
	
	<!-- Text Archive Button -->
		
	<!-- View Options Button -->
		<input type="image" src="/WebCat_Images/Castellano/Buttons/Link/VIEWOPT.gif" alt="VER OPCIONES" title="VER OPCIONES" name="VOPTIONS">
	
	<!-- Capture Button -->
		<input type="image" src="/WebCat_Images/Castellano/Buttons/Link/PRINTCAP.gif" alt="Imprimir o enviar por correo los registros guardados" title="Imprimir o enviar por correo los registros guardados" name="CAPTURE">
	
	<!-- hidden ebook processing -->
	
		<!-- gateway's custom buttons -->
	
	
	
	
	
	
	
		 <a href="/uhtbin/cgisirsi/?ps=lFsVn4GrQd/x/165390243/58" title="Desconexión" target="_top"><img src="/WebCat_Images/Castellano/Buttons/Link/EXITCAT.gif" border="0" alt="Desconexión" title="Desconexión"></a>
	
		</td>
	 </tr>
	</tbody></table>
	<a name="skipnav"></a>
		 <!-- if no library qualifier specified in search -->
		<!-- Print any WEBIMAGE tags that should appear before the list of tags -->
	
	<!-- begin routine to discover/discern enrichment types for this item (also netLibrary, URL and DMA -->
	 <!-- counter for enr types that builds content in iB/iL -->
	 <!-- counter for enr types that open up a new window -->
	
	<!-- Dynamic content lookup for disc_enrich.h -->
	
	
		 <!-- content_exists_any --> 
	
	 <!-- ibistro configured with content -->
	
	
	 <!-- show image links for URL or DMA tags (placed with enrichment) -->
					 
					 
					 
					 
					 
					 
					 
					 
					 
					 
					 
					 
					 
					 
					 
	
	<!-- end of disc_enrich.h -->
	<!-- end routine -->
	
	<!-- Find appropriate call number to display from list of call numbers -->
	<input type="hidden" name="first_hit" value="1">
	<input type="hidden" name="last_hit" value="1">
	
	<p class="searchsum" align="center">
	<!-- Print the message, if one exists (except for "volume does not exist",
	"This item has been marked lost" and "This item is assumed lost") -->
	
	
			registro
			1
			de
			1
			para la búsqueda
	<!--  Copyright (c) 2000 - 2003, Sirsi Corporation - Catalog Keyword search summary; iBistro -->
	<!-- Print the search summary -->
	<strong>
		Todos los campos
			"diseño de compiladores"
	
	
	
	
	
	
	
	</strong>
	</p>
		
	<div id="contentholder" class="contentholder">
	<table border="0" cellpadding="10" cellspacing="0">
	 <tbody><tr>
		<td valign="top" align="center" width="25%">
	
	<!-- dynamic content lookup for 5_item_services.h -->
	 <!-- ibistro configured with content -->
	
	<div class="itemservices">
		<div align="center">
		<img src="http://content.sirsidynixasp.co.uk/uhtbin/getenrichGL3-1.cgi?isbn=8479087005/MC.GIF&amp;client=sirsi&amp;type=rw12" border="0" alt="Portada">
		</div>
	 <!-- ibistro configured with content -->
	 <div align="center">
	 <script language="JavaScript" type="text/javascript">
		 put_keepremove_button("262262", "Guardar");
	 </script><img name="ickey-262262" src="/WebCat_Images/Castellano/Other/Miscil/clear.gif" alt="Guardar" border="0">
	<input type="button" class="itemdetails" name="ckey-262262" id="ckey-262262" value="Guardar" alt="Guardar" onclick="javascript:updatekeptlist(this,262262);">
	
	 </div>
	<!-- Only show the HOLD buttons if no E-BOOKs exist -->
					 <!-- hold link for no copies avail -->
			 <!-- hold icon -->
						
	
	<!-- Only show the BUYNOW  buttons if no E-BOOKs exist -->
		<!-- optionally show the BUYNOW buttons if no copies available -->
			 <!-- BUYNOW -->
		 <!-- BUYNOW only if not available -->
	 <!-- EBOOK -->
	
	
	<!-- only use if LIKESEARCH type is not set to EXACT -->
	<!--  Copyright (c) 2000 - 2003, Sirsi Corporation -  Related Search Button - These variables must be defined before including this file: - ENTRY_TYPE - tag entry type character to build the buttons for. - LINK_NAME - name of href link. -->
	
	
	
	
	
													<!-- Single term in tag -->
	
	
	
	
	
	
													<!-- Single term in tag -->
	
	
	
	
	
	
			<a href="/uhtbin/cgisirsi/?ps=g12hqqtU7m/x/165390243/18/XAU/XAUTHOR/Garrido+Alenda,+Alicia+OR+Universidad+de+Alicante+Departamento+de+Lenguajes+y+Sistemas+Inform%E1ticos">Más&nbsp;documentos&nbsp;de&nbsp;este&nbsp;autor</a>
	
	
	<!--  Copyright (c) 2000 - 2003, Sirsi Corporation -  Related Search Button - These variables must be defined before including this file: - ENTRY_TYPE - tag entry type character to build the buttons for. - LINK_NAME - name of href link. -->
	
	
	
	
	
													<!-- Single term in tag -->
	
	
	
	
	
	
													<!-- Single term in tag -->
	
	
	
	
	
	
													<!-- Single term in tag -->
	
	
	
	
	
	
													<!-- Single term in tag -->
	
	
	
	
	
	
			<a href="/uhtbin/cgisirsi/?ps=3yAqngwnsE/x/165390243/18/XSU/XSUBJECT/Programas+y+sistemas+de+programaci%F3n+OR+Lenguajes+de+programaci%F3n+OR+Compiladores+(Programas+y+sistemas+de+programaci%F3n)+OR+Compilaci%F3n+(Ordenadores)">Más&nbsp;documentos&nbsp;de&nbsp;estas&nbsp;materias</a>
	
	
	
	<!-- Find appropriate call number to display from list of call numbers -->
	
	
	<!-- Print call number browse search-->
			<a href="/uhtbin/cgisirsi/?ps=uK26M0gFt9/x/165390243/19/DP+136439/|NO|ALPHANUM">Documentos en la misma estantería</a>
			 
	
		 
	
	<!--  Copyright (c) 2000 - 2007, SirsiDynix - Unicorn Other Searches -->
	
	<!-- when search field is not blank, assign term to ENGINE_TERM -->
	
	
	
	<div class="enrichheader">Continuar la búsqueda en</div>
	
	
	
	
	
	<a href="javascript:open_win('http://www.google.com/search?q=diseño de compiladores&amp;safe=vss&amp;vss=1&amp;sa=Google+Search')">Google</a>
	
	
	
				
	
	
	
	<!--  Copyright (c) 2000, 2003 Sirsi Corporation - Cross Reference "quick-view" box. This page file is processed by a SIRSI_Command for an So response. -->
	 <!-- if xref list present -->
	</div>
		</td>
		<td align="left" valign="top"> <!-- tab container -->
		 <!-- show tabbed view if suported by browser and the environment is configured to do so -->		
		<div id="tabholder" class="tabholder"> <!-- show tabs for the panel -->
	<!--  Build this tab only copies exist -->
		 <span id="tab1" class="tab" onclick="showPanel(1);" onmouseover="hover(this);" onmouseout="setState(1)" style="background-color: rgb(255, 255, 255); color: rgb(0, 102, 153);">
					Información de ejemplar
							
		 </span>
		 <!-- Build this tab only if any CONTENT1-type content exists -->
			 <span id="tab2" class="tab" onclick="showPanel(2);" onmouseover="hover(this);" onmouseout="setState(2)"> Información complementaria </span>
		 <span id="tab3" class="tab" onclick="showPanel(3);" onmouseover="hover(this);" onmouseout="setState(3)">Registro del catálogo </span>
	
		</div> <!-- end tabholder span -->
		 <!-- end conditional to show the tabs -->
		<div class="panelholder">
				<div id="panel1" class="panel" style="display: block;">
		<div class="bibinfo"> <!-- displays, author, title, etc on all panels -->
			 <!-- Print the title, if one exists -->
				
				 <strong>Diseño de compiladores</strong>
	
		 
		 
			
			<br>
		 
				<!-- Print the author, if one exists -->
				 &nbsp;&nbsp;&nbsp;&nbsp;Garrido Alenda, Alicia<br>
			 
		 
		 
		</div> 	
	<!-- dynamic content lookup for viewtop.h -->
	
		<!-- show the following div if there is a summary put in it -->
	
			<div class="summary">
			<!-- dynamic content lookup for viewtop.h -->
	
				 <!--copyright -->
				Este
	libro
	es
	una
	introducción
	a
	las
	técnicas
	de
	construcción
	de
	compiladores,
	aunque
	gran
	parte
	de
	sus
	contenidos
	pueden
	también
	aplicarse
	al
	diseño
	de
	otros
	programas
	de
	traducción
	entre
	lenguajesinformáticos.
	El
	libro
	aúna
	los
	principios
	teóricos
	y
	los
	aspectos
	prácticos
	de
	la
	materia,
	haciendo
	especial
	énfasis
	en
	el
	diseño
	de
	<br>
	<a href="javascript:showPanel(2);">leer más...</a>
	
			 <!-- summary -->
	
			</div>
		 <!-- summary processing -->
	 <!-- ibistro configured with content -->
	
	<div class="bibinfo2">
	<table border="0" cellpadding="2" cellspacing="0">
	
		 <!-- extract requested bib data -->
	
				<tbody><tr> <!-- Print publisher data -->
					<th class="viewmarctags" valign="top" width="25%">Editor:</th>
					<td class="viewmarctags">Universidad de Alicante</td>
				</tr>
			 <!-- Ju data -->
		<!-- iteminfo option1 -->
	
			 <tr> <!-- Print publication date -->			 
				 <th class="viewmarctags" valign="top">Fecha de pub:</th>
				 <td class="viewmarctags">D.L.2002</td>
			 </tr>
			<!-- Jv data -->
		<!-- iteminfo option2 -->
	
				<tr> <!-- Print page count -->
					<th class="viewmarctags" valign="top">Descripción física:</th>
					<td class="viewmarctags">IV,314 p.</td>
				</tr>
			 <!-- Jt data -->
		 <!-- iteminfo option3 -->
	 <!-- list LT -->
	
		 <!-- iteminfo option1 -->
	
		<!-- iteminfo option2 -->
	
		<!-- iteminfo option3 -->
	 <!-- list LT -->
	
		 <!-- iteminfo option1 -->
	
		<!-- iteminfo option2 -->
	
		<!-- iteminfo option3 -->
	 <!-- list LT -->
	
		 <!-- iteminfo option1 -->
	
		<!-- iteminfo option2 -->
	
		<!-- iteminfo option3 -->
	 <!-- list LT -->
	
		 <!-- iteminfo option1 -->
	
		<!-- iteminfo option2 -->
	
		<!-- iteminfo option3 -->
	 <!-- list LT -->
	
		 <!-- iteminfo option1 -->
	
		<!-- iteminfo option2 -->
	
		<!-- iteminfo option3 -->
	 <!-- list LT -->
	
		 <!-- iteminfo option1 -->
	
		<!-- iteminfo option2 -->
	
		<!-- iteminfo option3 -->
	 <!-- list LT -->
	
		 <!-- iteminfo option1 -->
	
		<!-- iteminfo option2 -->
	
		<!-- iteminfo option3 -->
	 <!-- list LT -->
	
		 <!-- iteminfo option1 -->
	
		<!-- iteminfo option2 -->
	
		<!-- iteminfo option3 -->
	 <!-- list LT -->
	
		 <!-- iteminfo option1 -->
	
		<!-- iteminfo option2 -->
	
		<!-- iteminfo option3 -->
	 <!-- list LT -->
	
		 <!-- iteminfo option1 -->
	
		<!-- iteminfo option2 -->
	
		<!-- iteminfo option3 -->
	 <!-- list LT -->
	
		 <!-- iteminfo option1 -->
	
		<!-- iteminfo option2 -->
	
		<!-- iteminfo option3 -->
	 <!-- list LT -->
	
		 <!-- iteminfo option1 -->
	
		<!-- iteminfo option2 -->
	
		<!-- iteminfo option3 -->
	 <!-- list LT -->
	
		 <!-- iteminfo option1 -->
	
		<!-- iteminfo option2 -->
	
		<!-- iteminfo option3 -->
	 <!-- list LT -->
	
		 <!-- iteminfo option1 -->
	
		<!-- iteminfo option2 -->
	
		<!-- iteminfo option3 -->
	 <!-- list LT -->
	 <!-- Print ISBN number, if exists -->
		<tr>
		 <th class="viewmarctags" valign="top">ISBN:</th>
		 <td class="viewmarctags">8479087005</td>
		</tr>
		 
	 <!--list_of_available/holdings -->
		<tr>
		 <th class="viewmarctags" valign="top">
				 Info copia:</th>
					
		 <td class="viewmarctags">
			<!-- show if catalog or call-num item view -->
				 <!-- single library -->
		
			23 copias disponibles.<br>
		
			 <!-- single library system -->
				25 copias en todas las localizaciones.&nbsp;
				
		 </td>
		</tr>
		 <!-- show following row if enrichment data is available -->
			<tr><th class="viewmarctags" width="25%">Información complementaria</th>
		<td class="viewmarctags">
				<!-- dynamic content lookup -->
	
	
	
	
	
	
					<a href="javascript:showPanel(2);"><img src="/WebCat_Images/Castellano/Special/Link/SUMMARY.gif" border="0" alt="Resumen" title="Resumen"></a>
					<a href="javascript:showPanel(2);"><img src="/WebCat_Images/Castellano/Special/Link/TOC.gif" border="0" alt="Tabla de contenidos" title="Tabla de contenidos"></a>
	
	
	 <!-- ibistro configured with content -->
	
	
	
	
	
			 <!-- show image links for URL or DMA tags -->
		<!-- URL-type tag -->
	
		<!-- URL-type tag -->
	
		<!-- URL-type tag -->
	
		<!-- URL-type tag -->
	
		<!-- URL-type tag -->
	
		<!-- URL-type tag -->
	
		<!-- URL-type tag -->
	
		<!-- URL-type tag -->
	
		<!-- URL-type tag -->
	
		<!-- URL-type tag -->
	
		<!-- URL-type tag -->
	
		<!-- URL-type tag -->
	
		<!-- URL-type tag -->
	
		<!-- URL-type tag -->
	
		<!-- URL-type tag -->
	
			</td>
		 </tr>    	
	 </tbody></table>
	</div>
	
	 <!-- show if catalog or call-num item view -->
	<!-- check for the existence of MARC Holdings data -->
	
		 <!-- show holdings -->
	<!--  Copyright (c) 1996 - 2003, Sirsi Corporation -- Copy Holdings for a Single Item View; iBistro -->
	
	<a name="holdings"></a>
	<div class="enrichheader">
			Fondos
	</div>
	<table border="0" cellpadding="3" cellspacing="0">
				<!-- holdings allowed -->
				<!-- new library -->
			 <tbody><tr> <!-- Print library header line -->
		<td class="holdingsheader" colspan="4" align="left">
		</td>
			</tr>
			<tr>
				<td class="holdingsheader" align="left">
					Signatura
		</td>
		<td class="holdingsheader" align="right">Copia</td>
					<!-- displaying holds -->
					<td class="holdingsheader" align="right">Reservas</td>
					<td class="holdingsheader" align="left">Localización</td>
			</tr>
	
	
			<tr>
					<!-- Number of copies -->
				<!-- Start new callnum -->
				 <td class="holdingslist" align="left">DP 136439</td>
	
					<td class="holdingslist" align="right">0500748366</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">
							Depósito
					</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
	
				<!-- holdings allowed -->
	
	
			<tr>
					<!-- Number of copies -->
				<!-- Start new callnum -->
				 <td class="holdingslist" align="left">FL 004/DIS/GAR</td>
	
					<td class="holdingslist" align="right">500375359</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">
							Biblioteca de FL-1ª planta
					</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
			 <!-- Item Note -->
			 <tr>
			</tr><tr>
					 <td class="holdingslist">&nbsp;</td>
				 <td class="holdingslist" colspan="3" align="left">
	
					Nota:
		[reimp.] (cop. 2005)
	
				</td>
			 </tr>
	
				<!-- holdings allowed -->
	
	
			<tr>
					<!-- Number of copies -->
				<!-- Start new callnum -->
				 <td class="holdingslist" align="left">POE 004.4'4/DIS/DIS</td>
	
					<td class="holdingslist" align="right">500185920</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">
							Biblioteca Politécnica y Enfermería
					</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
	
				<!-- holdings allowed -->
	
	
			<tr>
					<td class="holdingslist" align="left">&nbsp;</td>
	
					<td class="holdingslist" align="right">500185573</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">
							Biblioteca Politécnica y Enfermería
					</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
	
				<!-- holdings allowed -->
	
	
			<tr>
					<td class="holdingslist" align="left">&nbsp;</td>
	
					<td class="holdingslist" align="right">500185574</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">
							Biblioteca Politécnica y Enfermería
					</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
	
				<!-- holdings allowed -->
	
	
			<tr>
					<td class="holdingslist" align="left">&nbsp;</td>
	
					<td class="holdingslist" align="right">500185575</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">
							Biblioteca Politécnica y Enfermería
					</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
	
				<!-- holdings allowed -->
	
	
			<tr>
					<td class="holdingslist" align="left">&nbsp;</td>
	
					<td class="holdingslist" align="right">500194184</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">
							Biblioteca Politécnica y Enfermería
					</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
	
				<!-- holdings allowed -->
	
	
			<tr>
					<td class="holdingslist" align="left">&nbsp;</td>
	
					<td class="holdingslist" align="right">500194185</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">
							Biblioteca Politécnica y Enfermería
					</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
	
				<!-- holdings allowed -->
	
	
			<tr>
					<td class="holdingslist" align="left">&nbsp;</td>
	
					<td class="holdingslist" align="right">500304014</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">
							Biblioteca Politécnica y Enfermería
					</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
	
				<!-- holdings allowed -->
	
	
			<tr>
					<td class="holdingslist" align="left">&nbsp;</td>
	
					<td class="holdingslist" align="right">500327179</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">
							Biblioteca Politécnica y Enfermería
							nocirc
					</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
	
				<!-- holdings allowed -->
	
	
			<tr>
					<td class="holdingslist" align="left">&nbsp;</td>
	
					<td class="holdingslist" align="right">500333384</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">
							Biblioteca Politécnica y Enfermería
					</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
	
				<!-- holdings allowed -->
	
	
			<tr>
					<td class="holdingslist" align="left">&nbsp;</td>
	
					<td class="holdingslist" align="right">500333385</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">
							Biblioteca Politécnica y Enfermería
					</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
	
				<!-- holdings allowed -->
	
	
			<tr>
					<td class="holdingslist" align="left">&nbsp;</td>
	
					<td class="holdingslist" align="right">500333386</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">devolución: 4/4/2017</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
	
				<!-- holdings allowed -->
	
	
			<tr>
					<td class="holdingslist" align="left">&nbsp;</td>
	
					<td class="holdingslist" align="right">500333387</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">
							Biblioteca Politécnica y Enfermería
					</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
	
				<!-- holdings allowed -->
	
	
			<tr>
					<td class="holdingslist" align="left">&nbsp;</td>
	
					<td class="holdingslist" align="right">500333388</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">
							Biblioteca Politécnica y Enfermería
					</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
	
				<!-- holdings allowed -->
	
	
			<tr>
					<td class="holdingslist" align="left">&nbsp;</td>
	
					<td class="holdingslist" align="right">500333389</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">
							Biblioteca Politécnica y Enfermería
					</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
	
				<!-- holdings allowed -->
	
	
			<tr>
					<td class="holdingslist" align="left">&nbsp;</td>
	
					<td class="holdingslist" align="right">500333390</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">
							Biblioteca Politécnica y Enfermería
					</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
	
				<!-- holdings allowed -->
	
	
			<tr>
					<td class="holdingslist" align="left">&nbsp;</td>
	
					<td class="holdingslist" align="right">500333401</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">
							Biblioteca Politécnica y Enfermería
					</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
	
				<!-- holdings allowed -->
	
	
			<tr>
					<td class="holdingslist" align="left">&nbsp;</td>
	
					<td class="holdingslist" align="right">500437665</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">
							Biblioteca Politécnica y Enfermería
							nocirc
					</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
	
				<!-- holdings allowed -->
	
	
			<tr>
					<td class="holdingslist" align="left">&nbsp;</td>
	
					<td class="holdingslist" align="right">500437666</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">
							Biblioteca Politécnica y Enfermería
					</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
	
				<!-- holdings allowed -->
	
	
			<tr>
					<td class="holdingslist" align="left">&nbsp;</td>
	
					<td class="holdingslist" align="right">0500568010</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">
							Biblioteca Politécnica y Enfermería
					</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
	
				<!-- holdings allowed -->
	
	
			<tr>
					<td class="holdingslist" align="left">&nbsp;</td>
	
					<td class="holdingslist" align="right">0500662923</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">devolución: 30/10/2017</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
	
				<!-- holdings allowed -->
	
	
			<tr>
					<td class="holdingslist" align="left">&nbsp;</td>
	
					<td class="holdingslist" align="right">0500680544</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">
							Biblioteca Politécnica y Enfermería
					</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
	
				<!-- holdings allowed -->
	
	
			<tr>
					<td class="holdingslist" align="left">&nbsp;</td>
	
					<td class="holdingslist" align="right">0500781946</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">
							Biblioteca Politécnica y Enfermería
					</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
	
				<!-- holdings allowed -->
	
	
			<tr>
					<td class="holdingslist" align="left">&nbsp;</td>
	
					<td class="holdingslist" align="right">0500782417</td>
					<td class="holdingslist" align="center">No</td>
					<td class="holdingslist" align="left">
							Biblioteca Politécnica y Enfermería
					</td>
	
				</tr>
	
	
			<!-- Boundwith holdings -->
	
	
	
	</tbody></table>
	
	
	
		
		
				</div>
	
				 <!-- check if an enrichment panel is needed -->	
				<div id="panel2" class="panel">
				 <!-- don't show the repeating bib info unless using single-item tabbed view -->
		<div class="bibinfo"> <!-- displays, author, title, etc on all panels -->
		 <!-- Print the title, if one exists -->
			<strong>Diseño de compiladores</strong>
			
			<br>
		
			 
		 <!-- Print the author, if one exists -->
			&nbsp;&nbsp;&nbsp;&nbsp;Garrido Alenda, Alicia<br>
		
		</div> 	
	<!--  Copyright (c) 2000 - 2007, SirsiDynix - Enrichments for single-item view. -->
	
	<!-- Determine which Enrichments are present -->
	
	<!-- Set the enrichment page variables if not already set. -->
	
	
	
	
	
	
	
	
	
	<a name="enrichments"></a>
	
	<!--  Copyright (c) 2000 - 2006, SirsiDynix- Generates one enrichment based on the ENRICHMENT variable which is either "TOC", "BIO", "SUM", "ACSUM", "REV", "LJREV", "SLJREV", BLREV", or "CHREV" for the type of enrichment. Relies on ENR_***_FILE to define the filepath of the enrichment file, where "***" is the ENRICHMENT variable. -->
	<!-- The Elib_revC iteration of one_enrich has disabled the "Read More" variable so that all enrichment data is parsed and presented on the screen. -->
	
	<!-- one_enrich.h -->
	
	<div class="enrichheader">
			Resumen
	</div>
	<div class="enrichcontent">
	
			Este libro es una introducción a las técnicas de construcción de compiladores, aunque gran parte de sus contenidos pueden también aplicarse al diseño de otros programas de traducción entre lenguajesinformáticos. El libro aúna los principios teóricos y los aspectos prácticos de la materia, haciendo especial énfasis en el diseño de traductores de lenguajes procedimentales. Al final de cada capítulo se proponen una serie de problemas, cuya solución puede encontrarse en uno de los apéndices. Asimismo, se incluyen algunos proyectos de programación que permiten asentar los conocimientos adquiridos.Los contenidos del texto son suficientes para organizar en torno a ellos un curso de "Procesadores de lenguaje", materia troncal en las titulaciones de Ingeniería en Informática.
			<span class="enrichtagline"></span>
	
	</div>
	
	
	
	
	
	<!--  Copyright (c) 2000 - 2006, SirsiDynix- Generates one enrichment based on the ENRICHMENT variable which is either "TOC", "BIO", "SUM", "ACSUM", "REV", "LJREV", "SLJREV", BLREV", or "CHREV" for the type of enrichment. Relies on ENR_***_FILE to define the filepath of the enrichment file, where "***" is the ENRICHMENT variable. -->
	<!-- The Elib_revC iteration of one_enrich has disabled the "Read More" variable so that all enrichment data is parsed and presented on the screen. -->
	
	<!-- one_enrich.h -->
	
	<div class="enrichheader">
			Tabla de contenidos
	</div>
	<div class="enrichcontent">
	
			<table border="0" cellpadding="3" cellspacing="0" align="center">
	<tbody><tr><td align="left" class="enrichcontent">
	Prólogo1 Introducción</td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 1.1 ¿Qué es un compilador? Tipos de compiladores </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 1.1.1 Tipos de compiladores </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 1.2 Historia de los primeros compiladores </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 1.2.1 El primer lenguaje y su compilador: FORTRAN </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 1.2.2 El lenguaje algorítmico ALGOL </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 1.2.3 Las primeras técnicas para desarrollar compiladores </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 1.2.4 Técnicas actuales para el desarrollo de compiladores</td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 1.3 Estructura de un compilador </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 1.3.1 Las fases de un compilador </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 1.3.2 Implementación del compilador a partir de las fases</td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 1.4 ¿Cómo se especifica un compilador? </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 1.5 Aplicaciones de estas técnicas </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 1.6 Referencias bibliográficas </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
	2 Análisis léxico</td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 2.1 El papel del analizador léxico </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 2.2 Errores léxicos </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 2.3 Funcionamiento del analizador léxico </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 2.4 Especificación de un analizador léxico </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 2.4.1 Definiciones de términos comunes en esta fase</td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 2.4.2 Identificación de palabras reservadas </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 2.5 Implementación de analizadores léxicos </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 2.5.1 Prioridad de tokens </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 2.6 Referencias bibliográficas </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 2.7 Ejercicios </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
	3 Análisis sintáctico</td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 3.1 La función del analizador sintáctico </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 3.2 Diseño de gramáticas </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 3.2.1 Recursividad </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 3.2.2 Ambigüedad </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 3.2.3 Asociatividad y precedencia de los operadores </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 3.3 Tipos de análisis sintáctico </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 3.4 Referencias bibliográficas </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 3.5 Ejercicios </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
	4 Análisis sintáctico descendente</td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 4.1 Introducción </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 4.1.1 Análisis con retroceso </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 4.1.2 Análizadores sintácticos predictivos </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 4.1.3 Conjuntos de predicción </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 4.2 Cálculo de los conjuntos de predicción </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 4.2.1 Cálculo del conjunto de primeros </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 4.2.2 Cálculo del conjunto de siguientes </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 4.2.3 Cálculo del conjunto predicción </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 4.3 La condición LL(1) </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 4.4 Modificación de gramáticas no LL(1) </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 4.4.1 Eliminación de la ambigüedad </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 4.4.2 Factorización por la izquierda </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 4.4.3 Eliminación de la recursividad por la izquierda </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 4.5 Analizador descendente recursivo </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 4.6 ASDP dirigidos por tabla </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 4.7 Manipulación de errores </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 4.8 Referencias bibliográficas </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 4.9 Ejercicios </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
	5 Análisis sintáctico ascendente</td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 5.1 Introducción </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 5.2 Análisis sintáctico por desplazamiento y reducción </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 5.3 Método SLR de construcción de tablas de análisis </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 5.3.1 Construcción de la colección canónica de conjuntos de elementos </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 5.3.2 Construcción de autómatas reconocedores de prefijos viables </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 5.3.3 Construcción de tablas SLR </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 5.3.4 Construcción de tablas SLR a partir del autómata reconocedor de prefijos viables </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 5.4 Conflictos en las tablas SLR </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 5.5 Mensajes de error en un analizador SLR </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 5.6 Clasificación de gramáticas </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 5.7 Referencias bibliográficas </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 5.8 Ejercicios                                   </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
	6 Traducción dirigida por la sintaxis              </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 6.1 Introducción </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 6.2 Gramáticas de atributos                      </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 6.3 Tipos de atributos                           </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 6.4 Grafos de dependencias                       </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 6.5 Especificación de un traductor               </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 6.5.1 Definiciones dirigidas por sintaxis    </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 6.5.2 Esquemas de traducción </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 6.6 Referencias bibliográficas </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 6.7 Ejercicios </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
	7 Implementación de traductores</td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 7.1 Introducción </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 7.2 Traductores descendentes recursivos </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 7.2.1 Eliminación de la recursividad izquierda </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 7.2.2 Factorización izquierda </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 7.2.3 Implementación de un traductor descendente recursivo</td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 7.3 Traductores ascendentes </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 7.3.1 Equivalencia entre estados y símbolos </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 7.3.2 Implementación de ETDS sencillos </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 7.3.3 Implementación de ETDS más complejos </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 7.3.4 Notación de YACC </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 7.3.5 ETDS con atributos heredados </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 7.3.6 Principales usos de los marcadores </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 7.4 Referencias bibliográficas </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 7.5 Ejercicios </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
	8 Tipos y generación de código</td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 8.1 Introducción </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 8.2 Gestión de la tabla de símbolos </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 8.3 Representaciones intermedias </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 8.4 Comprobaciones y conversiones de tipos </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 8.5 Código intermedio para expresiones </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 8.6 Código intermedio para instrucciones </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 8.7 Tipos compuestos </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 8.7.1 Tabla de tipos </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 8.7.2 Ámbitos y tabla de tipos </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 8.7.3 Equivalencia de tipos </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 8.8 Código intermedio para arrays </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 8.9 Código intermedio para registros </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 8.10 Referencias bibliográficas </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 8.11 Ejercicios </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
	9 Compilación de subprogramas</td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 9.1 Introducción </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 9.1.1 El entorno de ejecución </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 9.1.2 Registro de activación </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 9.1.3 Secuencias de llamada y retorno </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 9.1.4 Comprobaciones semánticas </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 9.1.5 Implementación con m2r </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 9.1.6 Valor devuelto </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 9.1.7 Gestión de la tabla de tipos </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 9.1.8 Parámetros y argumentos </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 9.2 Funciones sin recursividad </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 9.2.1 Compilación del cuerpo de la función </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 9.2.2 Compilación de la llamada a la función </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 9.3 Funciones con recursividad </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 9.3.1 Compilación del cuerpo de la función </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 9.3.2 Compilación de instrucciones </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 9.3.3 Compilación de la llamada </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 9.3.4 Traducción a m2r de la función factorial </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 9.4 Funciones locales </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 9.4.1 Encadenamiento de accesos </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 9.4.2 Display </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 9.5 Paso de parámetros </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 9.6 Referencias bibliográficas </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 9.7 Ejercicios </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
	</td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
	A. Soluciones a los ejercicios</td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 A.1 Soluciones a los ejercicios del capítulo 2 </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 A.2 Soluciones a los ejercicios del capítulo 3 </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 A.3 Soluciones a los ejercicios del capítulo 4 </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 A.4 Soluciones a los ejercicios del capítulo 5 </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 A.5 Soluciones a los ejercicios del capítulo 6 </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 A.6 Soluciones a los ejercicios del capítulo 7 </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 A.7 Soluciones a los ejercicios del capítulo 8 </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 A.8 Soluciones a los ejercicios del capítulo 9 </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
	</td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
	B. Ejercicios prácticos propuestos</td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 B.1 Analizador léxico </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 B.2 Analizador sintáctico descendente recursivo </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 B.3 Analizador SLR </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 B.4 Traductor descendente recursivo </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 B.5 Traductor ascendente </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 B.6 Compilador para un lenguaje sencillo </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 B.6.1 Especificación semántica </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 B.7 Compilador con tipos complejos </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 B.7.1 Especificación semántica </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
		 B.8 Compilador con funciones </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 B.8.1 Especificación semántica </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
				 B.8.2 Ampliación opcional: funciones locales </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
	C. El lenguaje intermedio m2r </td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
	</td>
	<td align="right" class="enrichcontent">
	</td></tr>
	<tr><td align="left" class="enrichcontent">
	Bibliografía</td>
	<td align="right" class="enrichcontent">
	</td></tr>
	</tbody></table>
	
	</div>
	
	<!-- check to see if any enrichment types of CONTENT2 are available -->
		<!-- ibistro configured with content -->
	
	
			 <!-- show image links for URL or DMA tags -->
	
	
						 
	
	
						 
	
	
						 
	
	
						 
	
	
						 
	
	
						 
	
	
						 
	
	
						 
	
	
						 
	
	
						 
	
	
						 
	
	
						 
	
	
						 
	
	
						 
	
	
						 
		<p></p>
				</div>
				<div id="panel3" class="panel">
				 <!-- don't show the repeating bib info unless using single-item tabbed view -->
		<div class="bibinfo"> <!-- displays, author, title, etc on all panels -->
		 <!-- Print the title, if one exists -->
			<strong>Diseño de compiladores</strong>
			
	<!-- View Options Button -->
		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
			<input type="image" src="/WebCat_Images/Castellano/Other/Miscil/VIEWOPT3.gif" alt="Cambiar visualización de catalogación" title="Cambiar visualización de catalogación" name="VOPTIONS">
			<br>
		
			 
		 <!-- Print the author, if one exists -->
			&nbsp;&nbsp;&nbsp;&nbsp;Garrido Alenda, Alicia<br>
		
		</div> 	
		
	<a name="marc_data"></a>
	
	
	<!-- The View Unformatted and Regular Views have been separated b/c of an additional column that has to appear for the indicators. The first conditional is to check to show unformatted, then the tables are then constructed using the list code. -->
	 <!-- view formatted -->
	
	<!-- Print the tags -->
	<table border="0" cellpadding="2" cellspacing="0" width="90%">
	 <!-- Print inline webimage-type tag -->
		 <!-- Regular tag -->
	 <tbody><tr>
		 <th class="viewmarctags" align="right" valign="top">
			 <!-- Regular tag -->
			ISBN
		</th>
		<td class="viewmarctags">
			84-7908-700-5
		</td>
	 </tr>
	 <!-- Print inline webimage-type tag -->
		 <!-- Regular tag -->
	 <tr>
		 <th class="viewmarctags" align="right" valign="top">
			 <!-- Regular tag -->
			CDU
		</th>
		<td class="viewmarctags">
			681.3.068
		</td>
	 </tr>
	 <!-- Print inline webimage-type tag -->
		 <!-- "Likeable" tag -->
	 <tr>
		<th class="viewmarctags" align="right" valign="top">
			Título
		</th>
		<td class="viewmarctags">
													<!-- Single term in tag -->
						<a href="/uhtbin/cgisirsi/?ps=22pSoIBHfO/x/165390243/18/XTITL/XTITLE/Dise%F1o+de+compiladores">Diseño de compiladores / Alicia Garrido Alenda ... [et al.]</a>      
		</td>
	 </tr>
	 <!-- Print inline webimage-type tag -->
		 <!-- Regular tag -->
	 <tr>
		 <th class="viewmarctags" align="right" valign="top">
			 <!-- Regular tag -->
			Publicación
		</th>
		<td class="viewmarctags">
			San Vicente del Raspeig (Alicante) : Universidad de Alicante, D.L.2002
		</td>
	 </tr>
	 <!-- Print inline webimage-type tag -->
		 <!-- Regular tag -->
	 <tr>
		 <th class="viewmarctags" align="right" valign="top">
			 <!-- Regular tag -->
			Descripción Física
		</th>
		<td class="viewmarctags">
			IV,314 p.
		</td>
	 </tr>
	 <!-- Print inline webimage-type tag -->
		 <!-- "Likeable" tag -->
	 <tr>
		<th class="viewmarctags" align="right" valign="top">
			Serie
		</th>
		<td class="viewmarctags">
													<!-- Single term in tag -->
						<a href="/uhtbin/cgisirsi/?ps=fdL7QRcFRP/x/165390243/18/X490/XSERIES/Textos+Dodentes">(Textos Dodentes)</a>      
		</td>
	 </tr>
	 <!-- Print inline webimage-type tag -->
		 <!-- Regular tag -->
	 <tr>
		 <th class="viewmarctags" align="right" valign="top">
			 <!-- Regular tag -->
			Nota General
		</th>
		<td class="viewmarctags">
			En la Port.: Departamento de Lenguajes y Sistemas Informáticos
		</td>
	 </tr>
	 <!-- Print inline webimage-type tag -->
		 <!-- Regular tag -->
	 <tr>
		 <th class="viewmarctags" align="right" valign="top">
			 <!-- Regular tag -->
			Nota General
		</th>
		<td class="viewmarctags">
			Existencias: [reimp.] (cop. 2005)
		</td>
	 </tr>
	 <!-- Print inline webimage-type tag -->
		 <!-- "Likeable" tag -->
	 <tr>
		<th class="viewmarctags" align="right" valign="top">
			Materia
		</th>
		<td class="viewmarctags">
													<!-- Single term in tag -->
						<a href="/uhtbin/cgisirsi/?ps=NAta2uunBL/x/165390243/18/X650/XSUBJECT/Programas+y+sistemas+de+programaci%F3n">Programas y sistemas de programación</a>      
		</td>
	 </tr>
	 <!-- Print inline webimage-type tag -->
		 <!-- "Likeable" tag -->
	 <tr>
		<th class="viewmarctags" align="right" valign="top">
			Materia
		</th>
		<td class="viewmarctags">
													<!-- Single term in tag -->
						<a href="/uhtbin/cgisirsi/?ps=3aG3IGPR4W/x/165390243/18/X650/XSUBJECT/Lenguajes+de+programaci%F3n">Lenguajes de programación</a>      
		</td>
	 </tr>
	 <!-- Print inline webimage-type tag -->
		 <!-- "Likeable" tag -->
	 <tr>
		<th class="viewmarctags" align="right" valign="top">
			Materia
		</th>
		<td class="viewmarctags">
													<!-- Single term in tag -->
						<a href="/uhtbin/cgisirsi/?ps=QJPdPm2wYG/x/165390243/18/X650/XSUBJECT/Compiladores+(Programas+y+sistemas+de+programaci%F3n)">Compiladores (Programas y sistemas de programación)</a>      
		</td>
	 </tr>
	 <!-- Print inline webimage-type tag -->
		 <!-- "Likeable" tag -->
	 <tr>
		<th class="viewmarctags" align="right" valign="top">
			Materia
		</th>
		<td class="viewmarctags">
													<!-- Single term in tag -->
						<a href="/uhtbin/cgisirsi/?ps=6G9S4iX0I6/x/165390243/18/X650/XSUBJECT/Compilaci%F3n+(Ordenadores)">Compilación (Ordenadores)</a>      
		</td>
	 </tr>
	 <!-- Print inline webimage-type tag -->
		 <!-- "Likeable" tag -->
	 <tr>
		<th class="viewmarctags" align="right" valign="top">
			Autor Secundario
		</th>
		<td class="viewmarctags">
													<!-- Single term in tag -->
						<a href="/uhtbin/cgisirsi/?ps=yABikM58IR/x/165390243/18/X700/XAUTHOR/Garrido+Alenda,+Alicia">Garrido Alenda, Alicia</a>      
		</td>
	 </tr>
	 <!-- Print inline webimage-type tag -->
		 <!-- "Likeable" tag -->
	 <tr>
		<th class="viewmarctags" align="right" valign="top">
			Entidad Secundaria
		</th>
		<td class="viewmarctags">
													<!-- Single term in tag -->
						<a href="/uhtbin/cgisirsi/?ps=Y5yB5uyRFy/x/165390243/18/X710/XAUTHOR/Universidad+de+Alicante+Departamento+de+Lenguajes+y+Sistemas+Inform%E1ticos">Universidad de Alicante. Departamento de Lenguajes y Sistemas Informáticos</a>      
		</td>
	 </tr>
	 <!-- Print inline webimage-type tag -->
		 <!-- "Likeable" tag -->
	 <tr>
		<th class="viewmarctags" align="right" valign="top">
			Serie
		</th>
		<td class="viewmarctags">
													<!-- Single term in tag -->
						<a href="/uhtbin/cgisirsi/?ps=McmSQbd6Hl/x/165390243/18/X830/XSERIES/Textos+Docentes+(Universidad+de+Alicante)">Textos Docentes (Universidad de Alicante)</a>      
		</td>
	 </tr>
	</tbody></table><!--end of bib cell-->
	
	 <!-- Print any WEBIMAGE tags that should appear after the list of tags -->
		
		<br clear="all">
				</div>
	
			</div> <!-- div container for content panels -->
		</td> <!-- end container cell -->
	 </tr>
	</tbody></table>
	</div> <!-- contentholder div -->
	
	<input type="hidden" name="form_type" value="">
	<!--  Copyright (c) 2000 - 2008, SirsiDynix - Buttons for Item View page, state #5. -->
	<table border="0" cellpadding="0" cellspacing="0" width="100%" class="gatewaystyle">
	 <tbody><tr>
		<td class="gatewaystyle">
	
		 <!-- Go back button -->
		 <a href="/uhtbin/cgisirsi/?ps=PPHmPfoXsL/x/165390243/2/18" title="VOLVER"><img src="/WebCat_Images/Castellano/Buttons/Link/GOBACK.gif" border="0" alt="VOLVER" title="VOLVER"></a>
	
		<!-- Help button -->
		<script language="JavaScript" type="text/javascript">
			put_help_button('Castellano','AYUDA','full_details');
		</script><a href="#" onclick="javascript:open_help_win('/iBistro_helps/User/Castellano/index.htm?context=elibrary&amp;topic=full_details')" alt="AYUDA" title="AYUDA"><img src="/WebCat_Images/Castellano/Buttons/Link/HELP.gif" border="0" alt="AYUDA" title="AYUDA"></a>
	
		
		<a href="/uhtbin/cgisirsi/?ps=vfRgI7wJN9/x/165390243/49" title="NUEVA BÚSQUEDA"><img src="/WebCat_Images/Castellano/Buttons/Link/NSEARCH.gif" border="0" alt="NUEVA BÚSQUEDA" title="NUEVA BÚSQUEDA"></a>
	
	<!-- Backward button -->
		<img src="/WebCat_Images/Castellano/Buttons/Link/UNBACKWARD.gif" border="0" alt="">
	
	<!-- Forward button -->
		<img src="/WebCat_Images/Castellano/Buttons/Link/UNFORWARD.gif" border="0" alt="">
	
	<!-- Cross Reference button -->
	
	<!-- Text Archive Button -->
		
	<!-- View Options Button -->
		<input type="image" src="/WebCat_Images/Castellano/Buttons/Link/VIEWOPT.gif" alt="VER OPCIONES" title="VER OPCIONES" name="VOPTIONS">
	
	<!-- Capture Button -->
		<input type="image" src="/WebCat_Images/Castellano/Buttons/Link/PRINTCAP.gif" alt="Imprimir o enviar por correo los registros guardados" title="Imprimir o enviar por correo los registros guardados" name="CAPTURE">
	
	<!-- hidden ebook processing -->
	
		<!-- gateway's custom buttons -->
	
	
	
	
	
	
	
		 <a href="/uhtbin/cgisirsi/?ps=4vUr9sL0Hh/x/165390243/58" title="Desconexión" target="_top"><img src="/WebCat_Images/Castellano/Buttons/Link/EXITCAT.gif" border="0" alt="Desconexión" title="Desconexión"></a>
	
		</td>
	 </tr>
	</tbody></table>
	<a name="skipnav"></a>
	</form>
	
	<!--  Copyright (c) 2000 - 2003, Sirsi Corporation - LC Category hidden search form for javascript to work. -->
	<form name="lc_search_form" method="post" action="/uhtbin/cgisirsi/?ps=1gBdjow3OV/x/165390243/5/5/25/1">
		<input type="hidden" name="searchdata1" value="">
		<input type="hidden" name="search_disp_data1" value="">
	</form>
	
	<form name="lc_return_form" method="post" action="/uhtbin/cgisirsi/?ps=hBBaU2BaFH/x/165390243/5/0/25/0">
		<input type="hidden" name="searchdata1" value="">
		<input type="hidden" name="sort_by" value="TI">
	</form>
	
	
	<br>
	<!--  Copyright (c) 1996 - 2009, SirsiDynix - Copyright statement -->
	<table border="0" cellpadding="3" cellspacing="0" width="100%" class="footer">
	 <tbody><tr>
		<td align="center" valign="bottom" width="15%" class="footer">
				<img src="/WebCat_Images/Castellano/Other/Miscil/sirsi_button.gif" alt="Powered by: SirsiDynix" border="0">
		</td>
		<td align="center" class="footer"><!-- Display the description -->
	
		 Biblioteca<br>Universidad de Alicante<br><br><br> 
		 <br>
			 Copyright © 2000 - 2009, SirsiDynix
		</td>
		<td align="center" width="15%" class="footer"><a name="bottom" href="#top">ARRIBA</a></td>
	 </tr>
	</tbody></table>
	</div> <!-- Controls Page Border -->
	
	
	
	
	
	
	
	</body></html>'''