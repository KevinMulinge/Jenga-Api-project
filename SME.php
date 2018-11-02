<?php
#echo "python Complete.py -c ".$_POST['Country']." -ta ".$_POST['Amount']." -dan ".$_POST['Number']." -dn ".$_POST['Name'];
$variable = <<<XYZ
<html>

<head>
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <link rel="stylesheet" href="qfc-dark.css">
  <link rel="stylesheet" href="nav.css">
  <!-- <link rel="stylesheet" href="qfc-light.css"> -->
      
 
<title>Send money within Equity</title>
</head>

<body>
     <ul id="menu">
    <li><a href="#">Options</a>
        <ul>
            <li><a href="index.html">Homepage</a></li>
            <li><a href="Send_Money_Within_Equity.html">Send Money within Equity</a></li>
            <li><a href="To_Mobile_Wallet.html">Send Money to Mobile Wallets</a></li>
            <li><a href="#">RTGS</a></li>
            <li><a href="#">SWIFT</a></li>
            <li><a href="#">EFT</a></li>
            <li><a href="#">Pesalink To Bank Account</a></li>
            <li><a href="#">Pesalink To Mobile Number</a></li>
            <li><a href="index.html">View Transactions</a></li>
        </ul>
    </li>
    
</ul>               
  <div class="qfc-container">
  <h>Feed back : <br>
XYZ;
echo $variable;
echo shell_exec("python SME.py -c ".$_POST['Country']." -ta ".$_POST['Amount']." -dan ".$_POST['Number']." -dn ".$_POST['Name']);
?>