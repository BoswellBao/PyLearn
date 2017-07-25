from __future__ import print_function
from testlink.testlinkapi  import TestlinkAPIClient
from testlink.testlinkhelper import TestLinkHelper
from testlink.testlinkerrors import TLResponseError
import sys, os.path
from platform import python_version

# precondition a)
# SERVER_URL and KEY are defined in environment
# TESTLINK_API_PYTHON_SERVER_URL=http://YOURSERVER/testlink/lib/api/xmlrpc.php
# TESTLINK_API_PYTHON_DEVKEY=7ec252ab966ce88fd92c25d08635672b
#
# alternative precondition b)
# SERVEUR_URL and KEY are defined as command line arguments
# python TestLinkExample.py --server_url http://YOURSERVER/testlink/lib/api/xmlrpc.php
#                           --devKey 7ec252ab966ce88fd92c25d08635672b
#
# ATTENTION: With TestLink 1.9.7, cause of the new REST API, the SERVER_URL
#            has changed from
#               (old) http://YOURSERVER/testlink/lib/api/xmlrpc.php
#            to
#               (new) http://YOURSERVER/testlink/lib/api/xmlrpc/v1/xmlrpc.php
tl_helper = TestLinkHelper(server_url="http://192.168.1.67/testlink/lib/api/xmlrpc/v1/xmlrpc.php", devkey="9fcab75a07b343c40fbe91c98a1bb326")
tl_helper.setParamsFromArgs('''Shows how to use the TestLinkAPI.
=> Counts and lists the Projects 
=> Create a new Project with the following structure:''')
myTestLink = tl_helper.connect(TestlinkAPIClient)

myPyVersion = python_version()   # 本地python版本
myPyVersionShort = myPyVersion.replace('.', '')[:2]

NEWTESTPLAN_A = "TestPlan_API A"
NEWTESTPLAN_B = "TestPlan_API B"
NEWTESTPLAN_C = "TestPlan_API C - DeleteTest"
NEWPLATFORM_A = 'Big Birds %s' % myPyVersionShort
NEWPLATFORM_B = 'Small Birds'
NEWPLATFORM_C = 'Ugly Birds'
NEWTESTSUITE_A = "A - First Level"
NEWTESTSUITE_B = "B - First Level"
NEWTESTSUITE_AA = "AA - Second Level"
NEWTESTCASE_AA = "TESTCASE_AA"
NEWTESTCASE_B = "TESTCASE_B"
myApiVersion = '%s v%s' % (myTestLink.__class__.__name__, myTestLink.__version__)
NEWBUILD_A = '%s' % myApiVersion
NEWBUILD_B = '%s' % myApiVersion
NEWBUILD_C = '%s - DeleteTest' % myApiVersion
NEWBUILD_D = '%s - copyTestersTest' % myApiVersion

this_file_dirname = os.path.dirname(__file__)    # mytestlink
NEWATTACHMENT_PY = os.path.join(this_file_dirname, 'TestLinkExample.py')
NEWATTACHMENT_PNG = os.path.join(this_file_dirname, 'PyGreat.png')

# Servers TestLink Version
myTLVersion = myTestLink.testLinkVersion()   # testlink版本
myTLVersionShort = myTLVersion.replace('.', '')

NEWPROJECT = "NEW_PROJECT_API-%s" % myPyVersionShort
NEWPREFIX = "NPROAPI%s" % myPyVersionShort
ITSNAME = "myITS"

# used connection settings
print(myTestLink.connectionInfo())
print("")

# CHANGE this name into a valid account, known in your TL application
myTestUserName = "admin"
myTestUserName2 = "admin"
# get user information    # 获取用户信息
response = myTestLink.getUserByLogin(myTestUserName)
print("getUserByLogin", response)
myTestUserID = response[0]['dbID']
response = myTestLink.getUserByID(myTestUserID)
print("getUserByID   ", response)

# example asking the api client about methods arguments
print(myTestLink.whatArgs('assignTestCaseExecutionTask'))

# example handling Response Error Codes
# first check an invalid devKey and than the own one
try:
    myTestLink.checkDevKey(devKey='9fcab75a07b343c40fbe91c98a1bb326')
except TLResponseError as tl_err:
    if tl_err.code == 2000:
        # expected invalid devKey Error
        # now check the own one - just call with default settings
        myTestLink.checkDevKey()
    else:
        # seems to be another response failure - we forward it
        raise

print("Number of Projects in TestLink: %s " % (myTestLink.countProjects()))   # 获取项目的总数
print("")
a = myTestLink.listProjects()   # 分别列出项目名称和项目id
print(type(a))


# Delete the project, if it already exists
try:
    response = myTestLink.deleteTestProject(NEWPREFIX)
    print("deleteTestProject", response)
except TLResponseError:
    print("No project with prefix %s exists" % NEWPREFIX)

# get IssueTrackerSystem   问题跟踪系统，目前没有集成
# aITS=myTestLink.getIssueTrackerSystem(ITSNAME)
# print("getIssueTrackerSystem", aITS)

# Creates the project   创建项目,表nodes_hierarchy,testprojects
projInfo = 'Example created with Python %s API class %s in TL %s' % \
           (python_version(), myApiVersion, myTLVersion)
newProject = myTestLink.createTestProject(NEWPROJECT, NEWPREFIX,    # 新建项目页面的一些参数
                                          notes=projInfo, active=1, public=1,
                                          #    itsname=ITSNAME, itsenabled=1,
                                          options={'requirementsEnabled': 0, 'testPriorityEnabled': 1,
                                                   'automationEnabled': 1, 'inventoryEnabled': 0})
print("createTestProject", newProject)
newProjectID = newProject[0]['id']
print(newProject[0])
print("New Project '%s' - id: %s" % (NEWPROJECT, newProjectID))

# Creates the test plan    创建测试计划 表nodes_hierarchy，testplans
newTestPlan = myTestLink.createTestPlan(NEWTESTPLAN_A, testprojectname=NEWPROJECT,
                                        notes='New TestPlan created with the API', active=1, public=1)
print("createTestPlan", newTestPlan)
print(newTestPlan[0])
newTestPlanID_A = newTestPlan[0]['id']
print("New Test Plan '%s' - id: %s" % (NEWTESTPLAN_A, newTestPlanID_A))

# Create test plan B  - uses no platforms    一般用上面的
newTestPlan = myTestLink.createTestPlan(NEWTESTPLAN_B, prefix=NEWPREFIX,
                                        notes='New TestPlan created with the Generic API - uses no platforms.',
                                        active=1, public=1)
print("createTestPlan", newTestPlan)
newTestPlanID_B = newTestPlan[0]['id']
print("New Test Plan '%s' - id: %s" % (NEWTESTPLAN_B, newTestPlanID_B))

# Create platform 'Big Birds x'    创建平台 表testplan_platforms
newPlatForm = myTestLink.createPlatform(NEWPROJECT, NEWPLATFORM_A,
                                        notes='Platform for Big Birds, unique name, only used in this project')
print("createPlatform", newPlatForm)
newPlatFormID_A = newPlatForm['id']
# Add Platform  'Big Bird x' to plan
response = myTestLink.addPlatformToTestPlan(newTestPlanID_A, NEWPLATFORM_A)
print("addPlatformToTestPlan", response)

# Create platform 'Small Birds'
newPlatForm = myTestLink.createPlatform(NEWPROJECT, NEWPLATFORM_B,
                                        notes='Platform for Small Birds, name used in all example projects')
print("createPlatform", newPlatForm)
newPlatFormID_B = newPlatForm['id']
# Add Platform  'Small Bird' to platform
response = myTestLink.addPlatformToTestPlan(newTestPlanID_A, NEWPLATFORM_B)
print("addPlatformToTestPlan", response)

# Create platform 'Ugly Birds'
newPlatForm = myTestLink.createPlatform(NEWPROJECT, NEWPLATFORM_C,
                                        notes='Platform for Ugly Birds, will be removed from test plan')
print("createPlatform", newPlatForm)
newPlatFormID_C = newPlatForm['id']
# Add Platform  'Ugly Bird' to platform
response = myTestLink.addPlatformToTestPlan(newTestPlanID_A, NEWPLATFORM_C)
print("addPlatformToTestPlan", response)

# Creates the test Suite A   创建测试用例集  表testsuites，nodes_hierarchy
print()
newTestSuite = myTestLink.createTestSuite(newProjectID, NEWTESTSUITE_A,
                                          "Details of the Test Suite A")
print("createTestSuite", newTestSuite)
newTestSuiteID_A = newTestSuite[0]['id']
print("New Test Suite '%s' - id: %s" % (NEWTESTSUITE_A, newTestSuiteID_A))

FirstLevelID = newTestSuiteID_A

# Creates the test Suite B
newTestSuite = myTestLink.createTestSuite(newProjectID, NEWTESTSUITE_B,
                                          "Details of the Test Suite B")
print("createTestSuite", newTestSuite)
newTestSuiteID_B = newTestSuite[0]['id']
print("New Test Suite '%s' - id: %s" % (NEWTESTSUITE_B, newTestSuiteID_B))

# Creates the test Suite AA    创建测试用例子集
newTestSuite = myTestLink.createTestSuite(newProjectID, NEWTESTSUITE_AA,
                                          "Details of the Test Suite AA", parentid=FirstLevelID)   # 多了parentid，指向父用例集
print("createTestSuite", newTestSuite)
newTestSuiteID_AA = newTestSuite[0]['id']
print("New Test Suite '%s' - id: %s" % (NEWTESTSUITE_AA, newTestSuiteID_AA))


## 测试用例
MANUAL = 1    # 手工的
AUTOMATED = 2    # 自动的
READFORREVIEW = 2    # 准备评审
REWORK = 4    # 重写
HIGH = 3    # 重要性：高
MEDIUM = 2    # 中
LOW = 1    # 低

# Creates the test case TC_AA  with state ready for review   表：nodes_hierarchy，tcversions，
myTestLink.initStep("Step action 1", "Step result 1", MANUAL)
myTestLink.appendStep("Step action 2", "Step result 2", MANUAL)
myTestLink.appendStep("Step action 3", "Step result 3", MANUAL)
myTestLink.appendStep("Step action 4", "Step result 4", MANUAL)
myTestLink.appendStep("Step action 5", "Step result 5", MANUAL)
myTestLink.appendStep("Dummy step for delete tests",
                      "should be delete with deleteTestCaseSteps", MANUAL)

newTestCase = myTestLink.createTestCase(NEWTESTCASE_AA, newTestSuiteID_AA,    # 参数：7用例名称，用例集id，项目id，编辑用例用户，摘要，前提，优先级，状态，估计执行时间
                                        newProjectID, myTestUserName, "This is the summary of the Test Case AA",
                                        preconditions='these are the preconditions',    # 默认手工的
                                        importance=LOW, state=READFORREVIEW, estimatedexecduration=10.1)
print("createTestCase", newTestCase)
newTestCaseID_AA = newTestCase[0]['id']
print("New Test Case '%s' - id: %s" % (NEWTESTCASE_AA, newTestCaseID_AA))

# Creates the test case TC_B  with state rework
myTestLink.initStep("Step action 1", "Step result 1", AUTOMATED)
myTestLink.appendStep("Step action 2", "Step result 2", AUTOMATED)
myTestLink.appendStep("Step action 3", "Step result 3", AUTOMATED)
myTestLink.appendStep("Step action 4", "Step result 4", AUTOMATED)
myTestLink.appendStep("Step action 5", "Step result 5", AUTOMATED)

newTestCase = myTestLink.createTestCase(NEWTESTCASE_B, newTestSuiteID_B,
                                        newProjectID, myTestUserName, "This is the summary of the Test Case B",
                                        preconditions='these are the preconditions', executiontype=AUTOMATED,    # 标志自动的
                                        status=REWORK, estimatedexecduration=0.5)
print("createTestCase", newTestCase)
newTestCaseID_B = newTestCase[0]['id']
print("New Test Case '%s' - id: %s" % (NEWTESTCASE_B, newTestCaseID_B))

# Add  test cases to test plan - we need the full external id !
# for every test case version 1 is used
tc_version = 1
# TC AA should be tested with platforms 'Big Birds'+'Small Birds'
tc_aa_full_ext_id = myTestLink.getTestCase(newTestCaseID_AA)[0]['full_tc_external_id']
response = myTestLink.addTestCaseToTestPlan(newProjectID, newTestPlanID_A,   # 把用例加到测试计划，参数：项目id，测试计划id，...,y用例版本，
                                            tc_aa_full_ext_id, tc_version, platformid=newPlatFormID_A)
print("ssssssss:",myTestLink.getTestCase(newTestCaseID_AA))
print("addTestCaseToTestPlan", response)
tc_aa_full_ext_id = myTestLink.getTestCase(newTestCaseID_AA)[0]['full_tc_external_id']
response = myTestLink.addTestCaseToTestPlan(newProjectID, newTestPlanID_A,
                                            tc_aa_full_ext_id, tc_version, platformid=newPlatFormID_B)
print("addTestCaseToTestPlan", response)
# change test case TC_AA - delete step 6 (step 7 does not exist)
response = myTestLink.deleteTestCaseSteps(tc_aa_full_ext_id, [7, 6],
                                          version=tc_version)
print("deleteTestCaseSteps", response)

# TC B should be tested with platform 'Small Birds'
tc_b_full_ext_id = myTestLink.getTestCase(testcaseid=newTestCaseID_B)[0]['full_tc_external_id']
response = myTestLink.addTestCaseToTestPlan(newProjectID, newTestPlanID_A,
                                            tc_b_full_ext_id, tc_version, platformid=newPlatFormID_B)
print("addTestCaseToTestPlan", response)

# Update test case TC_B -> high, change step 5, new step 6    # 用例创建步骤
steps_tc_b = myTestLink.getTestCase(testcaseid=newTestCaseID_B)[0]['steps']
steps_tc_b_v1u = steps_tc_b[:4]
steps_tc_b_v1u.append(
    {'step_number': 5, 'actions': "Step action 5 -b changed by updateTestCase",
     'expected_results': "Step result 5 - b changed", 'execution_type': AUTOMATED})
steps_tc_b_v1u.append(
    {'step_number': 6, 'actions': "Step action 6 -b added by updateTestCase",
     'expected_results': "Step result 6 - b added", 'execution_type': AUTOMATED})
response = myTestLink.updateTestCase(tc_b_full_ext_id, version=tc_version,
                                     steps=steps_tc_b_v1u, importance=MEDIUM, estimatedexecduration=3)
print("updateTestCase", response)

# create additional steps via createTestCaseSteps - action create
steps_tc_b_c67 = [
    {'step_number': 6, 'actions': "action 6 createTestCaseSteps.create",
     'expected_results': "skip - cause step 6 already exist", 'execution_type': AUTOMATED},
    {'step_number': 7, 'actions': "action 7 createTestCaseSteps.create",
     'expected_results': "create - cause step 7 not yet exist", 'execution_type': AUTOMATED}]
response = myTestLink.createTestCaseSteps('create', steps_tc_b_c67,
                                          testcaseexternalid=tc_b_full_ext_id, version=tc_version)
print("createTestCaseSteps.create", response)
# create additional steps via createTestCaseSteps - action update
steps_tc_b_c38 = [
    {'step_number': 3, 'actions': "action 3 createTestCaseSteps.update",
     'expected_results': "update - cause step 3 already exist", 'execution_type': AUTOMATED},
    {'step_number': 8, 'actions': "action 8 createTestCaseSteps.update",
     'expected_results': "create - cause step 8 not yet exist", 'execution_type': AUTOMATED}]
response = myTestLink.createTestCaseSteps('update', steps_tc_b_c38,
                                          testcaseid=newTestCaseID_B, version=tc_version)
print("createTestCaseSteps.update", response)

# In test plan B TC B  should be tested without  platform
response = myTestLink.addTestCaseToTestPlan(newProjectID, newTestPlanID_B,
                                            tc_b_full_ext_id, tc_version)
print("addTestCaseToTestPlan", response)

# # Try to Remove Platform  'Big Birds' from platform
# response = myTestLink.removePlatformFromTestPlan(newTestPlanID_A, NEWPLATFORM_C)
# print "removePlatformFromTestPlan", response

# Remove Platform  'Ugly Birds' from platform
response = myTestLink.removePlatformFromTestPlan(newTestPlanID_A, NEWPLATFORM_C)
print("removePlatformFromTestPlan", response)

# -- Create Build for TestPlan A (uses platforms)    # 为测试计划创建版本
newBuild = myTestLink.createBuild(newTestPlanID_A, NEWBUILD_A,
                                  'Notes for the Build', releasedate="2016-12-31")
print("createBuild", newBuild)
newBuildID_A = newBuild[0]['id']
print("New Build '%s' - id: %s" % (NEWBUILD_A, newBuildID_A))

# assign user to test case execution tasks - test plan with platforms    # 分配测试用例
response = myTestLink.assignTestCaseExecutionTask(myTestUserName,
                                                  newTestPlanID_A, tc_aa_full_ext_id,
                                                  buildid=newBuildID_A, platformname=NEWPLATFORM_A)
print("assignTestCaseExecutionTask", response)
response = myTestLink.assignTestCaseExecutionTask(myTestUserName2,
                                                  newTestPlanID_A, tc_aa_full_ext_id,
                                                  buildname=NEWBUILD_A, platformid=newPlatFormID_B)
print("assignTestCaseExecutionTask", response)
response = myTestLink.assignTestCaseExecutionTask(myTestUserName,
                                                  newTestPlanID_A, tc_b_full_ext_id,
                                                  buildname=NEWBUILD_A, platformname=NEWPLATFORM_B)
print("assignTestCaseExecutionTask", response)

# get test case assigned tester    # 获取测试用例分配的人员
response = myTestLink.getTestCaseAssignedTester(
    newTestPlanID_A, tc_aa_full_ext_id,
    buildid=newBuildID_A, platformname=NEWPLATFORM_A)
print("getTestCaseAssignedTester TC_AA TP_A Platform A", response)
response = myTestLink.getTestCaseAssignedTester(
    newTestPlanID_A, tc_aa_full_ext_id,
    buildname=NEWBUILD_A, platformid=newPlatFormID_B)
print("getTestCaseAssignedTester TC_AA TP_A Platform B", response)
response = myTestLink.getTestCaseAssignedTester(
    newTestPlanID_A, tc_b_full_ext_id,
    buildname=NEWBUILD_A, platformname=NEWPLATFORM_B)
print("getTestCaseAssignedTester TC_B TP_A Platform B", response)

# get bugs for test case TC_AA in test plan A - state TC not executed
response = myTestLink.getTestCaseBugs(newTestPlanID_A,
                                      testcaseexternalid=tc_aa_full_ext_id)
print("getTestCaseBugs TC_AA in TP_A (TC is not executed)", response)

# report Test Case Results for platform 'Big Bird' with step results    # 测试用例执行结果
# TC_AA failed, build should be guessed, TC identified with external id
newResult = myTestLink.reportTCResult(None, newTestPlanID_A, None, 'f', '', guess=True,
                                      testcaseexternalid=tc_aa_full_ext_id,
                                      platformname=NEWPLATFORM_A,
                                      execduration=3.9, timestamp='2015-09-18 14:33',
                                      steps=[
                                          {'step_number': 3, 'result': 'p', 'notes': 'result note for passed step 3'},
                                          {'step_number': 4, 'result': 'f', 'notes': 'result note for failed step 4'}])
print("reportTCResult", newResult)
newResultID_AA = newResult[0]['id']

# get bugs for test case TC_AA in test plan A - state TC is executed
response = myTestLink.getTestCaseBugs(newTestPlanID_A,
                                      testcaseexternalid=tc_aa_full_ext_id)
print("getTestCaseBugs TC_AA in TP_A (TC is executed, no bug)", response)

# report Test Case Results for platform 'Small Bird'    # 平台测试结果报告
# TC_AA passed, build should be guessed, TC identified with external id
newResult = myTestLink.reportTCResult(None, newTestPlanID_A, None, 'p', '', guess=True,
                                      testcaseexternalid=tc_aa_full_ext_id,
                                      platformname=NEWPLATFORM_B,
                                      execduration='2.2', timestamp='2015-09-19 14:33:02')
print("reportTCResult", newResult)
newResultID_AA_p = newResult[0]['id']
# TC_B passed, explicit build and some notes , TC identified with internal id
newResult = myTestLink.reportTCResult(newTestCaseID_B, newTestPlanID_A, NEWBUILD_A,
                                      'p', 'first try', platformname=NEWPLATFORM_B)
print("reportTCResult", newResult)
newResultID_B = newResult[0]['id']

# # add this (text) file as Attachemnt to last execution of TC_B  with
# # different filename 'MyPyExampleApiClient.py'
# a_file = open(NEWATTACHMENT_PY)
# newAttachment = myTestLink.uploadExecutionAttachment(a_file, newResultID_B,
#                                                      'Textfile Example',
#                                                      'Text Attachment Example for a TestCase Execution',
#                                                      filename='MyPyExampleApiClient.py')
# print("uploadExecutionAttachment", newAttachment)
# # add png file as Attachemnt to last execution of TC_AA
# # !Attention - on WINDOWS use binary mode for none text file
# # see http://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
# a_file = open(NEWATTACHMENT_PNG, mode='rb')
# newAttachment = myTestLink.uploadExecutionAttachment(a_file, newResultID_AA,
#                                                      'PNG Example', 'PNG Attachment Example for a TestCase Execution')
# print("uploadExecutionAttachment", newAttachment)

# -- Create Build for TestPlan B (uses no platforms)
newBuild = myTestLink.createBuild(newTestPlanID_B, NEWBUILD_B,
                                  'Build for TestPlan without platforms', releasedate='2016-11-30')
print("createBuild", newBuild)
newBuildID_B = newBuild[0]['id']
print("New Build '%s' - id: %s" % (NEWBUILD_B, newBuildID_B))

# assign user to test case execution tasks - test plans without platforms
response = myTestLink.assignTestCaseExecutionTask(myTestUserName,
                                                  newTestPlanID_B, tc_b_full_ext_id, buildname=NEWBUILD_B)
print("assignTestCaseExecutionTask", response)

# get test case assigned tester
response = myTestLink.getTestCaseAssignedTester(
    newTestPlanID_B, tc_b_full_ext_id, buildname=NEWBUILD_B)
print("getTestCaseAssignedTester TC_B TP_B no Platform", response)

# try to remove not assigned tester    # 从分配的用例移除用户
response = myTestLink.unassignTestCaseExecutionTask(
    newTestPlanID_B, tc_b_full_ext_id, buildname=NEWBUILD_B,
    user=myTestUserName2)
print("unassignTestCaseExecutionTask not assigned user", response)
response = myTestLink.getTestCaseAssignedTester(
    newTestPlanID_B, tc_b_full_ext_id, buildname=NEWBUILD_B)
print("getTestCaseAssignedTester TC_B TP_B no Platform", response)

# try to remove all assigned tester
response = myTestLink.unassignTestCaseExecutionTask(
    newTestPlanID_B, tc_b_full_ext_id, buildid=newBuildID_B,
    action='unassignAll')
print("unassignTestCaseExecutionTask unassignAll", response)
response = myTestLink.getTestCaseAssignedTester(
    newTestPlanID_B, tc_b_full_ext_id, buildname=NEWBUILD_B)
print("getTestCaseAssignedTester TC_B TP_B no Platform", response)

# reassign user to test case execution tasks - test plans without platforms    # 重新分配用例
response = myTestLink.assignTestCaseExecutionTask(myTestUserName,
                                                  newTestPlanID_B, tc_b_full_ext_id, buildid=newBuildID_B)
print("assignTestCaseExecutionTask", response)
response = myTestLink.getTestCaseAssignedTester(
    newTestPlanID_B, tc_b_full_ext_id, buildname=NEWBUILD_B)
print("getTestCaseAssignedTester TC_B TP_B no Platform", response)

# TC_B blocked (without platform), explicit build and some notes ,
# TC identified with internal id, report by myTestUserName
newResult = myTestLink.reportTCResult(newTestCaseID_B, newTestPlanID_B, NEWBUILD_B,
                                      'f', "no birds are singing", bugid='007',
                                      user=myTestUserName)
print("reportTCResult", newResult)
newResultID_B_f = newResult[0]['id']
newResult = myTestLink.reportTCResult(newTestCaseID_B, newTestPlanID_B, NEWBUILD_B,
                                      'b', "hungry birds blocks the execution",
                                      bugid='008', user=myTestUserName)
print("reportTCResult", newResult)
newResultID_B_b = newResult[0]['id']
# get bugs for test case TC_B in test plan B - state TC is executed with bug
response = myTestLink.getTestCaseBugs(newTestPlanID_B,
                                      testcaseid=newTestCaseID_B)
print("getTestCaseBugs TC_B in TP_B (TC is executed with 2 bugs)", response)

# now we make a mistake and commit the same result a second time
# and try to delete this mistake
newResult = myTestLink.reportTCResult(newTestCaseID_B, newTestPlanID_B, NEWBUILD_B,
                                      'b', "mistake, commit same result a second time")
print("reportTCResult", newResult)
newResultID_B_b2 = int(newResult[0]['id'])
try:
    # if TL configuration allows deletion of executions, no error will occur
    response = myTestLink.deleteExecution(newResultID_B_b2)
    print("deleteExecution", response)
except TLResponseError as tl_err:
    if tl_err.code == 232:
        # TL configuration does not allow deletion of executions
        pass
    else:
        # sh..: another problem occurs
        raise

# now we try to change the execution types of the test cases
# - AA from manual -> auto  and B from auto -> manual
newResult = myTestLink.setTestCaseExecutionType(tc_aa_full_ext_id, tc_version,
                                                newProjectID, AUTOMATED)
print("setTestCaseExecutionType", response)
newResult = myTestLink.setTestCaseExecutionType(tc_b_full_ext_id, tc_version,
                                                newProjectID, MANUAL)
print("setTestCaseExecutionType", response)

# create TestPlan C with Platform, Build , TestCase, assigned TestCase
# and delete it
newTestPlan = myTestLink.createTestPlan(NEWTESTPLAN_C, NEWPROJECT,
                                        notes='TestPlan for delete test.',
                                        active=1, public=1)
print("createTestPlan for DeleteTest", newTestPlan)
newTestPlanID_C = newTestPlan[0]['id']
print("Test Plan '%s' - id: %s" % (NEWTESTPLAN_C, newTestPlanID_C))
newBuild = myTestLink.createBuild(newTestPlanID_C, NEWBUILD_C,
                                  'Build for TestPlan delete test')
print("createBuild for DeleteTest", newBuild)
newBuildID_C = newBuild[0]['id']
print("Build '%s' - id: %s" % (NEWBUILD_C, newBuildID_C))
response = myTestLink.addPlatformToTestPlan(newTestPlanID_C, NEWPLATFORM_C)
print("addPlatformToTestPlan", response)
response = myTestLink.addTestCaseToTestPlan(newProjectID, newTestPlanID_C,
                                            tc_aa_full_ext_id, tc_version, platformid=newPlatFormID_C)
print("addTestCaseToTestPlan", response)
response = myTestLink.assignTestCaseExecutionTask(myTestUserName,
                                                  newTestPlanID_C, tc_aa_full_ext_id, buildid=newBuildID_C,
                                                  platformid=newPlatFormID_C)
print("assignTestCaseExecutionTask", response)
newResult = myTestLink.reportTCResult(newTestCaseID_AA, newTestPlanID_C,
                                      NEWBUILD_C, 'p', "TP delete test",
                                      platformname=NEWPLATFORM_C)
print("reportTCResult", newResult)
newResultID_B = newResult[0]['id']
# newAttachment = myTestLink.uploadExecutionAttachment(NEWATTACHMENT_PY, newResultID_B,
#                                                      'Textfile Example',
#                                                      'Attachment Example for a TC Execution and TP delete test',
#                                                      filename='MyPyTPDeleteTest.py')
# print("uploadExecutionAttachment", newAttachment)
# response = myTestLink.getTotalsForTestPlan(newTestPlanID_C)
# print("getTotalsForTestPlan before delete", response)
# response = myTestLink.deleteTestPlan(newTestPlanID_C)
# print("deleteTestPlan", response)
# try:
#     response = myTestLink.getTotalsForTestPlan(newTestPlanID_C)
#     print("getTotalsForTestPlan after delete", response)
# except TLResponseError as tl_err:
#     print(tl_err.message)

# -- Create Build D and copy Testers from Build A    # 创建新的版本并复制执行人
newBuild = myTestLink.createBuild(newTestPlanID_A, NEWBUILD_D,
                                  'Build with copied testers from Build ' + NEWBUILD_A,
                                  active=1, open=1, copytestersfrombuild=newBuildID_A)
print("createBuild", newBuild)
newBuildID_D = newBuild[0]['id']
print("New Build '%s' - id: %s" % (NEWBUILD_D, newBuildID_D))

# get information - TestProject    # 获取项目信息
response = myTestLink.getTestProjectByName(NEWPROJECT)    # 通过名字找项目
print("getTestProjectByName", response)
response = myTestLink.getProjectTestPlans(newProjectID)    # 通过项目id获取所有测试计划
print("getProjectTestPlans", response)
response = myTestLink.getFirstLevelTestSuitesForTestProject(newProjectID)    # 通过项目id获取所有一级测试用例集
print("getFirstLevelTestSuitesForTestProject", response)
response = myTestLink.getProjectPlatforms(newProjectID)    # 通过项目id获取平台
print("getProjectPlatforms", response)
response = myTestLink.getProjectKeywords(newProjectID)    # 通过项目id获取关键字
print("getProjectKeywords", response)

# get information - testPlan    # 获取测试计划信息
response = myTestLink.getTestPlanByName(NEWPROJECT, NEWTESTPLAN_A)    # 通过项目名字，计划名字获取测试计划
print("getTestPlanByName", response)
response = myTestLink.getTotalsForTestPlan(newTestPlanID_A)
print("getTotalsForTestPlan", response)
response = myTestLink.getBuildsForTestPlan(newTestPlanID_A)    # 通过测试计划id获取所有测试版本
print("getBuildsForTestPlan", response)
response = myTestLink.getLatestBuildForTestPlan(newTestPlanID_A)    # 通过测试计划id获取最新的测试版本
print("getLatestBuildForTestPlan", response)
response = myTestLink.getTestPlanPlatforms(newTestPlanID_A)    # 通过测试计划id获取计划所在的平台
print("getTestPlanPlatforms", response)
response = myTestLink.getTestSuitesForTestPlan(3)     # 通过测试计划id获取测试用例集——有用
print("getTestSuitesForTestPlan", response)
myTestLink.getTestCasesForTestSuite()
# get failed Testcases
# # -- Start CHANGE v0.4.5 --
# # response = myTestLink.getTestCasesForTestPlan(newTestPlanID_A, 'executestatus=f')
response = myTestLink.getTestCasesForTestPlan(newTestPlanID_A, executestatus='f')    # 通过计划id获取执行失败的用例
# # -- END CHANGE v0.4.5 --
print("getTestCasesForTestPlan A failed ", response)
# # get Testcases for Plattform SmallBird
# response = myTestLink.getTestCasesForTestPlan(newTestPlanID_A, platformid=newPlatFormID_B)
# print("getTestCasesForTestPlan A SmallBirds", response)
#
# get information - TestSuite
response = myTestLink.getTestSuiteByID(newTestSuiteID_B)    # 通过测试用例集id获取用例集
print("getTestSuiteByID", response)
response = myTestLink.getTestSuitesForTestSuite(newTestSuiteID_A)    # 通过测试用例集id获取所有子用例集
print("getTestSuitesForTestSuite A", response)
response = myTestLink.getTestCasesForTestSuite(newTestSuiteID_A, True, 'full')    # 通过测试用例集id获取所有测试用例详细信息，和子集——有用
print("getTestCasesForTestSuite A", response)
response = myTestLink.getTestCasesForTestSuite(newTestSuiteID_B, False, 'only_id')    # 通过测试用例集id获取所有测试用例id，不显示子集
print("getTestCasesForTestSuite B", response)

# Update test suite B details - Using Project ID   #  更新测试用例
updatedTestSuite = myTestLink.updateTestSuite(newTestSuiteID_B,
                                              testprojectid=newProjectID,
                                              details="updated Details of the Test Suite B")
print("updateTestSuite", updatedTestSuite)

# Update test suite A name and order details - Using Project Name
# with TL 1.9.15 this step fails - solution see TL Mantis Ticket 7696
# <http://mantis.testlink.org/view.php?id=7696>
changedNEWTESTSUITE_A = NEWTESTSUITE_A + ' - Changed'    # 更新测试用例集
updatedTestSuite = myTestLink.updateTestSuite(newTestSuiteID_A, prefix=NEWPREFIX,
                                              testsuitename=changedNEWTESTSUITE_A, order=1)
print("updateTestSuite", updatedTestSuite)

# get all test suites, using the same name - test Suite B
response = myTestLink.getTestSuite(NEWTESTSUITE_B, NEWPREFIX)
print("getTestSuite", response)

# # get informationen - TestCase
# # -- Start CHANGE v0.4.5 --
# # response = myTestLink.getTestCaseIDByName(NEWTESTCASE_B, None, NEWPROJECT)
response = myTestLink.getTestCaseIDByName(NEWTESTCASE_B, testprojectname=NEWPROJECT)    # 通过测试用例名找测试用例id
# # -- END CHANGE v0.4.5 --
print("getTestCaseIDByName", response)
tcpathname = '::'.join([NEWPROJECT, changedNEWTESTSUITE_A, NEWTESTSUITE_AA, NEWTESTCASE_AA])
response = myTestLink.getTestCaseIDByName('unknown', testcasepathname=tcpathname)
print("getTestCaseIDByName", response)
# get execution result
response = myTestLink.getLastExecutionResult(newTestPlanID_A, None,    # 获取用例最近一次的执行结果
                                             testcaseexternalid=tc_aa_full_ext_id)
print("getLastExecutionResult", response)
response = myTestLink.getLastExecutionResult(newTestPlanID_A, newTestCaseID_B)
print("getLastExecutionResult", response)
# if not myTLVersion == '<= 1.9.8':
#     # new optional arguments platformid , buildid with TL 1.9.9
#     response = myTestLink.getLastExecutionResult(
#         newTestPlanID_A, newTestCaseID_AA,
#         platformid=newPlatFormID_A)
#     print("getLastExecutionResult", response)
#
# response = myTestLink.getExecCountersByBuild(newTestPlanID_A)
# print("getExecCountersByBuild", response)
# response = myTestLink.getExecCountersByBuild(newTestPlanID_B)
# print("getExecCountersByBuild", response)
# response = myTestLink.getTestCaseKeywords(testcaseexternalid=tc_b_full_ext_id)
# print("getTestCaseKeywords noKeyWords", response)
#
# get information - general
response = myTestLink.getFullPath(int(newTestSuiteID_AA))    # 通过测试集id获取路径。或者多个
print("getFullPath", response)
response = myTestLink.getFullPath([int(newTestCaseID_AA), int(newTestCaseID_B)])
print("getFullPath", response)

# # attachments
# # add png file as Attachment to test project
# a_file = open(NEWATTACHMENT_PNG, mode='rb')
# newAttachment = myTestLink.uploadTestProjectAttachment(a_file, newProjectID,
#                                                        title='PNG Example',
#                                                        description='PNG Attachment Example for a TestProject')
# print("uploadTestProjectAttachment", newAttachment)
# # add png file as Attachnent to test suite A - uploadXxzAttachmemt also file path
# newAttachment = myTestLink.uploadTestSuiteAttachment(NEWATTACHMENT_PNG, newTestSuiteID_A,
#                                                      title='PNG Example',
#                                                      description='PNG Attachment Example for a TestSuite')
# print("uploadTestSuiteAttachment", newAttachment)
# # add png file as Attachment to test case B
# a_file = open(NEWATTACHMENT_PNG, mode='rb')
# newAttachment = myTestLink.uploadTestCaseAttachment(a_file, newTestCaseID_B,
#                                                     title='PNG Example',
#                                                     description='PNG Attachment Example for a TestCase')
# print("uploadTestCaseAttachment", newAttachment)
# # get Attachment of test case B
# # response = myTestLink.getTestCaseAttachments(testcaseexternalid=tc_aa_full_ext_id)
# # print "getTestCaseAttachments", response
# response = myTestLink.getTestCaseAttachments(testcaseid=newTestCaseID_B)
# print("getTestCaseAttachments", response)
#
# copy test case - as a new TC version  # 复制用例
# print("create new version of TC B")
# response = myTestLink.copyTCnewVersion(newTestCaseID_B,
#                                        summary='new version of TC B', importance='1')
# print('copyTCnewVersion', response)
#
# # copy test case - as new TC in a different TestSuite
# print("copy TC B as TC BA into Test suite A")
# response = myTestLink.copyTCnewTestCase(newTestCaseID_B,
#                                         testsuiteid=newTestSuiteID_A, testcasename='%sA' % NEWTESTCASE_B)
# print('copyTCnewTestCase', response)
# response = myTestLink.getTestCasesForTestSuite(newTestSuiteID_B, False, 'simple')
# print('getTestCasesForTestSuite B', response)
# response = myTestLink.getTestCasesForTestSuite(newTestSuiteID_A, True, 'simple')
# print('getTestCasesForTestSuite A', response)
#
# # sample, how the test plan can be updated to use the new tc version
# # site effect of this step, assigned testers and existing execution results are
# # not accessible anymore via the TL Web Gui.
# # That is the reason, why we have uncomment it for the normal sample execution
# # response = myTestLink.addTestCaseToTestPlan(newProjectID, newTestPlanID_B,
# #                                             tc_b_full_ext_id, tc_version+1,
# #                                             overwrite=1)
# # print("addTestCaseToTestPlan overwrite", response)
#
#
# # no test data
# # response = myTestLink.getTestCaseCustomFieldDesignValue(
# #             tc_aa_full_ext_id, 1, newProjectID, 'cfieldname', 'simple')
# # print "getTestCaseCustomFieldDesignValue", response
# print("getTestCaseCustomFieldDesignValue", "Sorry currently no testdata")
#
# # add png file as Attachemnt to a requirement specification.
# print("uploadRequirementSpecificationAttachment", "Sorry currently no testdata")
# # add png file as Attachemnt to a requirement.
# print("uploadRequirementAttachment", "Sorry currently no testdata")
#
# # add requirements to testcase AA
# # response = myTestLink.assignRequirements(tc_aa_full_ext_id, newProjectID,
# #                         [{'req_spec' : 6729, 'requirements' : [6731]},
# #                          {'req_spec' : 6733, 'requirements' : [6735, 6737]}])
# print("assignRequirements", "Sorry currently no testdata")
#
print("")
print("Number of Projects      in TestLink: %s " % myTestLink.countProjects())
print("Number of Platforms  (in TestPlans): %s " % myTestLink.countPlatforms())
print("Number of Builds                   : %s " % myTestLink.countBuilds())
print("Number of TestPlans                : %s " % myTestLink.countTestPlans())
print("Number of TestSuites               : %s " % myTestLink.countTestSuites())
print("Number of TestCases (in TestSuites): %s " % myTestLink.countTestCasesTS())
print("Number of TestCases (in TestPlans) : %s " % myTestLink.countTestCasesTP())
print("")

print()
print("")
myTestLink.listProjects()