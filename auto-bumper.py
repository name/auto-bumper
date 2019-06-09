from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'braiden'
passwordStr = 'DR6ZXovN'

browser = webdriver.Chrome()
browser.get(('https://ogusers.com/member.php?action=login'))

browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Username/Email:'])[1]/following::input[1]").click()
browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Username/Email:'])[1]/following::input[1]").clear()
browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Username/Email:'])[1]/following::input[1]").send_keys(usernameStr)
browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[1]").click()
browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[1]").clear()
browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[1]").send_keys(passwordStr)
browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[3]").click()

browser.get(('https://ogusers.com/Thread-add-me-on-steam--382587'))
browser.find_element_by_id("message").click()
browser.find_element_by_id("message").clear()
browser.find_element_by_id("message").send_keys("bumping to the top ty")
browser.find_element_by_id("quick_reply_submit").click()

#<form action="member.php" method="post">
#<input type="hidden" name="action" value="do_login" />
#<input type="hidden" name="url" value="" />
#<input name="my_post_key" type="hidden" value="12e663d63b9ce6b94ff5cab54de08a2b" />
#<input type="hidden" name="quick_login" value="1" />
#<table border="0" cellspacing="0" cellpadding="5" class="trim-container" style="width: 320px;border: 0">
#<tr>
#<td class="maintitle" colspan="2" style="font-size: 12px; text-transform: uppercase;">
#<strong>Login to OGUsers.com</strong>
#</td>
#</tr>
#<tr>
#<td class="col_row">
#<div class="inputstyle">
#<label class="input">
#<input type="text" class="textbox" name="username" size="25" value="" placeholder="Username..." />
#</label>
#</div>
#</td>
#</tr>
#<tr>
#<td class="col_row">
#<div class="inputstyle">
#<label class="input">
#<input type="password" class="textbox" name="password" size="25" value="" placeholder="Password..." />
#</label>
#</div>
#</td>
#</tr>
#<tr>
#<td class="col_row">
#<div class="inputstyle">
#<label class="input">
#<input type="password" class="textbox" name="2facode" size="25" placeholder="Enter 2FA Code (If enabled)" />
#</label>
#</div>
#</td>
#</tr>
#<tr>
#<td class="col_row">
#<div>
#<a href="member.php?action=lostpw">
#<div class="lostpass">
#Lost your password?
#</div>
#</a>
#</div>
#</td>
#</tr>
#<tr>
#<td class="col_row" align="center"><label title="If ticked, your login details will be remembered on this computer, otherwise, you will be logged out as soon as you close your browser."><input type="checkbox" class="checkbox" name="remember" checked="checked" value="yes" /> Remember me</label></td>
#</tr>
#<tr>
#<td style="padding: 0;">
#<input type="submit" class="loginpage" name="submit" value="Login" />
#</td>
#</tr>
#</table>
#</form>