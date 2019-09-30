import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
 
    def test_lower_identifier(self):
        """test lower identifiers"""
        testcase = "abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 101))

    def test_upper_identifier(self):
        """test upper identifier"""
        testcase = "AbC"
        expect = "AbC,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 102))

    def test_ID_with_underscore(self):
        """test ID with underscore"""
        testcase = "_abv__"
        expect = "_abv__,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 103))
    
    def test_one_underscore(self):
        """test underscore ID"""
        testcase = "_"
        expect = "_,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 104))

    def test_wrong_ID_1(self):
        """test wrong identifier 1"""
        testcase = "!__"
        expect = "!,__,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 105))

    def test_icon1(self):
        """test error_char 1"""
        testcase = "@__@"
        expect = "Error Token @"
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 106))
    
    def test_icon2(self):
        """test error_char 2"""
        testcase = "~__~"
        expect = "Error Token ~"
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 107))

    def test_icon3(self):
        """test error_char 3"""
        testcase = "|:3"
        expect = "Error Token |"
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 108))

    def test_integer(self):
        """test integer"""
        testcase = "123 001 , 123, 000_000"
        expect = "123,001,,,123,,,000,_000,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 109))

    def test_float(self):
        """test float number"""
        testcase = "1.2e1 10e-1 0.0 1.0e01 0.0e0 0.1e 000.1 123e"
        expect = "1.2e1,10e-1,0.0,1.0e01,0.0e0,0.1,e,000.1,123,e,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 110))

    def test_error_char(self):
        """test error char"""
        testcase = "#_abc_ "
        expect = "Error Token #"
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 111))

    def test_string(self):
        """test simple string"""
        testcase = "\"hello world\""
        expect = "hello world,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(testcase, expect, 112))
    
    def test_symbolic(sefl):
        """test symbolic"""
        testcase = "+-*/!&|"
        expect = "+,-,*,/,!,Error Token &"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 113))
    
    def test_symbolic_1(sefl):
        """test symbolic 1 """
        testcase = "==!==->=<><=><==>"
        expect = "==,!=,=,-,>=,<,>,<=,>,<=,=,>,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 114))

    def test_symbolic_2(sefl):
        """test symbolic 2 """
        testcase = "[=-=][+-+][=-=][>-<][T-T][:|]"
        expect = "[,=,-,=,],[,+,-,+,],[,=,-,=,],[,>,-,<,],[,T,-,T,],[,Error Token :"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 115))

    def test_symbolic_3(sefl):
        """test symbolic 3 """
        testcase = "[{ hello world "
        expect = "[,{,hello,world,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 116))

    def test_symbolic_4(sefl):
        """test symbolic 4 """
        testcase = "++--||&&**/;,"
        expect = "+,+,-,-,||,&&,*,*,/,;,,,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 117))

    def test_comment(sefl):
        """test line comment"""
        testcase = "// abvc \t \b \n"
        expect = "<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 118))
    
    def test_more_commnet(sefl):
        """test more comment"""
        testcase = """// abv /* abv */ 
                      // avc """
        expect = "<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 119))
    
    def test_block_comment(sefl):
        """test more comment"""
        testcase = """/*/ abv /* abv */ 
                      /*/ avc """
        expect = "/,*,/,avc,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 120))

    def test_block_comment_1(sefl):
        """test block comment_1"""
        testcase = """/*/ abv /*/// abv */ 
                      /*// avc """
        expect = "/,*,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 121))

    def test_block_comment_2(sefl):
        """test block comment_2"""
        testcase = """/*/ abc
                       * abc\n
                       *bc\t \\
                       */ """
        expect = "<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 122))

    def test_wrong_block_comment_3(sefl):
        """test wrong block comment_2"""
        testcase = """/* abv /* abv  
                      /* avc """
        expect = "/,*,abv,/,*,abv,/,*,avc,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 123))

    def test_int_type(sefl):
        """test int type"""
        testcase = "int"
        expect = "int,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 124))
    
    def test_float_type(sefl):
        """test float type"""
        testcase = "float"
        expect = "float,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 125))

    def test_string_type(sefl):
        """test string type"""
        testcase = "string"
        expect = "string,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 126))

    def test_bool_type(sefl):
        """test bool type"""
        testcase = "boolean"
        expect = "boolean,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 127))

    def test_void_type(sefl):
        """test void type"""
        testcase = "void"
        expect = "void,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 128))

    def test_truefalse(sefl):
        """test truefalse"""
        testcase = "truefalse"
        expect = "truefalse,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 129))

    def test_true_false(sefl):
        """test true_false"""
        testcase = "true false"
        expect = "true,false,<EOF>"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 130))
    
    def test_unclosed_string(sefl):
        """test unclosed string"""
        testcase = """ "hello world  """
        expect = "Unclosed String: hello world  "
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 131))
    
    def test_unclosed_string2(sefl):
        """test unclosed string2"""
        testcase = """ "hello world
                    """
        expect = "Unclosed String: hello world"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 132))
    
    def test_unclosed_string3(sefl):
        """test unclosed string3"""
        testcase = """ "hello world
                        " """
        expect = "Unclosed String: hello world"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 133))

    def test_unclosed_string4(sefl):
        """test unclosed string4"""
        testcase = """ "/*hello world*/ """
        expect = "Unclosed String: /*hello world*/ " 
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 134))

    def test_illeagal_escape(sefl):
        """test illegal escape"""
        testcase = """ "hello\\cworld" """
        expect = "Illegal Escape In String: hello\c"
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 135))
    
    def test_illeagal_escape2(sefl):
        """test illegal escape2"""
        testcase = """ "hello\\ world" """
        expect = "Illegal Escape In String: hello\ "
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 136))
    
    def test_combine_1(sefl):
        """test combine_1"""
        testcase = """ "hello\\" """
        expect = """Unclosed String: hello\\" """
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 137))
    
    def test_combine_2(sefl):
        """test combine_2"""
        testcase = """ abv"avc"ac" """
        expect = """abv,avc,ac,Unclosed String:  """
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 138))
    
    def test_combine_3(sefl):
        """test combine_3"""
        testcase = """\\ abc \k abv \n " """
        expect = """Error Token \\"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 139))
    
    def test_combine_4(sefl):
        """test combine_4"""
        testcase = """// abc \k abv \n " """
        expect = """Unclosed String:  """
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 140))
    
    def test_combine_5(sefl):
        """test combine_5"""
        testcase = """string a = "hello\\n world!" """
        expect = """string,a,=,hello\\n world!,<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 141))
    
    def test_combine_6(sefl):
        """test combine_5"""
        testcase = """string a = "hello\\b\\n world!" """
        expect = """string,a,=,hello\\b\\n world!,<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 142))
    
    def test_combine_7(sefl):
        """test combine_7"""
        testcase = """string a = "hello\\b\\pworld!" """
        expect = """string,a,=,Illegal Escape In String: hello\\b\\p"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 143))
    
    def test_combine_8(sefl):
        """test combine_8"""
        testcase = """string a = "hello\\b\\ world!" """
        expect = """string,a,=,Illegal Escape In String: hello\\b\\ """
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 144))
    

    def test_combine_9(sefl):
        """test combine_0"""
        testcase = """string a = "hello// world!" """
        expect = """string,a,=,hello// world!,<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 145))

    
    def test46(sefl):
        """test46"""
        testcase = """void main(){a,b;c,"as", "!", @"} """
        expect = """void,main,(,),{,a,,,b,;,c,,,as,,,!,,,Error Token @"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 146))
    
    def test47(sefl):
        """test47""" 
        testcase = """for(int i = 0; i < 10;1,3e1++)"""
        expect = """for,(,int,i,=,0,;,i,<,10,;,1,,,3e1,+,+,),<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 147))
    
    def test48(sefl):
        """test50""" 
        testcase = """abc+abc-abc-"abc"+1.2+000+1e1+1.1.1.1"""
        expect = """abc,+,abc,-,abc,-,abc,+,1.2,+,000,+,1e1,+,1.1,.1,.1,<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 148))

    def test49(sefl):
        """test49""" 
        testcase = """_+_/*__*\\_*?"""
        expect = """_,+,_,/,*,__,*,Error Token \\"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 149))

    def test50(sefl):
        """test50""" 
        testcase = """a > b : a ? b"""
        expect = """a,>,b,Error Token :"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 150))

    def test51(sefl):
        """test51"""
        testcase = """a >> b << c *// abc\n a>>b<<=c"""
        expect = """a,>,>,b,<,<,c,*,a,>,>,b,<,<=,c,<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 151))

    def test52(sefl):
        """test52"""
        testcase = """a/b/c/*a*/ = 1"""
        expect = """a,/,b,/,c,=,1,<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 152))
    
    def test53(sefl):
        """test53"""
        testcase = """#define 1 1.2e"""
        expect = """Error Token #"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 153))

    def test54(sefl):
        """test54"""
        testcase = """{do a + b while (a+b>1)}"""
        expect = """{,do,a,+,b,while,(,a,+,b,>,1,),},<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 154))
    
    def test55(sefl):
        """test55"""
        testcase = """1.e - 1e0 + 1.e-31 + 1e + e1.0 + 1.2e-1 + 1.-e"""
        expect = """1.,e,-,1e0,+,1.e-31,+,1,e,+,e1,.0,+,1.2e-1,+,1.,-,e,<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 155))
    
    def test56(sefl):
        """test56"""
        testcase = """a&b"""
        expect = """a,Error Token &"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 156))
    
    def test57(sefl):
        """test57"""
        testcase = """a|b"""
        expect = """a,Error Token |"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 157))
    
    def test58(sefl):
        """test58"""
        testcase = """//!@~$%^&&*\n ^"""
        expect = """Error Token ^"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 158))
    
    def test59(sefl):
        """test59"""
        testcase = """//!@~$%^&&*\b ^"""
        expect = """<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 159))
    
    def test60(sefl):
        """test60"""
        testcase = """int a = 1 + b / 2;"""
        expect = """int,a,=,1,+,b,/,2,;,<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 160))
    
    def test61(sefl):
        """test61"""
        testcase = """int main () {return "abc";"""
        expect = """int,main,(,),{,return,abc,;,<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 161))
    
    def test62(sefl):
        """test62"""
        testcase = """int main () {return "abc;"""
        expect = """int,main,(,),{,return,Unclosed String: abc;"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 162))
    
    def test63(sefl):
        """test63"""
        testcase = """return "abc
                    ;"""
        expect = """return,Unclosed String: abc"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 163))
    
    def test64(sefl):
        """test64"""
        testcase = """array[?] = 1;
                    ;"""
        expect = """array,[,Error Token ?"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 164))
    
    def test65(sefl):
        """test65"""
        testcase = """array[?] = 1;
                    ;"""
        expect = """array,[,Error Token ?"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 164))
    
    def test66(sefl):
        """test66"""
        testcase = """
        package hienthi;

        import inso.InSo;

        public class UseThread{
            public static void main(String[] args) {
                
                InSo insochan = new InSo(true);
                Thread thread_chan = new Thread(insochan);
                thread_chan.start();

                InSo insole = new InSo(false);
                Thread thread_le = new Thread(insole);
                thread_le.start();
            }
        }"""
        expect = """package,hienthi,;,import,inso,Error Token ."""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 166))
    
    def test67(sefl):
        """test67"""
        testcase = """a = b % c % d / 2;"""
        expect = """a,=,b,%,c,%,d,/,2,;,<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 167))
    
    def test68(sefl):
        """test68"""
        testcase = """int a[4] = true;
                    ;"""
        expect = """int,a,[,4,],=,true,;,;,<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 168))

    def test69(sefl):
        """test69"""
        testcase = """if while do else return ` ;"""
        expect = """if,while,do,else,return,Error Token `"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 169))

    def test70(sefl):
        """test70"""
        testcase = """ char ch = 'a';"""
        expect = """char,ch,=,Error Token '"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 170))
    
    def test71(sefl):
        """test71"""
        testcase = """////*/ """
        expect = """<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 171))

    def test72(sefl):
        """test72"""
        testcase = """abc_abc = "abc """
        expect = """abc_abc,=,Unclosed String: abc """
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 172))

    def test73(sefl):
        """test73"""
        testcase = """ "abc@\n" """
        expect = """Unclosed String: abc@"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 173))

    def test74(sefl):
        """test74"""
        testcase = """ "abc@\\b" """
        expect = """abc@\\b,<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 174))

    def test75(sefl):
        """test75"""
        testcase = """ "abc@\n\\b" """
        expect = """Unclosed String: abc@"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 175))
    
    def test76(sefl):
        """test76"""
        testcase = """ "abc@\\n\\fabc" """
        expect = """abc@\\n\\fabc,<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 176))

    def test77(sefl):
        """test77"""
        testcase = """ "abc@\\n\\fabc"\\ """
        expect = """abc@\\n\\fabc,Error Token \\"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 177))
    
    def test78(sefl):
        """test78"""
        testcase = """ "abc\\n\\abc" """
        expect = """Illegal Escape In String: abc\\n\\a"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 178))

    def test79(sefl):
        """test79"""
        testcase = """ "\n" """
        expect = """Unclosed String: """
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 179))
    
    def test80(sefl):
        """test80"""
        testcase = """ print("\\n"); """
        expect = """print,(,\\n,),;,<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 180))
    
    def test81(sefl):
        """test81"""
        testcase = """ //~!@#$\t\b
                        /nabc """
        expect = """/,nabc,<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 181))
    
    def test82(sefl):
        """test82"""
        testcase = """ a = "//\\//\\" """
        expect = """a,=,Illegal Escape In String: //\/"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 182))
    
    def test83(sefl):
        """test83"""
        testcase = """ /* helloworld
                        * helloworld 
                       /*/"""
        expect = """<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 183))

    def test84(sefl):
        """test84"""
        testcase = """ int a[9] = {1,2,3,4,5,6,,7,8,9} """
        expect = """int,a,[,9,],=,{,1,,,2,,,3,,,4,,,5,,,6,,,,,7,,,8,,,9,},<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 184))
    
    def test85(sefl):
        """test85"""
        testcase = """"""
        expect = """<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 185))
    
    def test86(sefl):
        """test86"""
        testcase = """a_-b_ = c_;"""
        expect = """a_,-,b_,=,c_,;,<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 186))
    

    def test87(sefl):
        """test87"""
        testcase = """string str = "\n"""
        expect = """string,str,=,Unclosed String: """
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 187))

    def test88(sefl):
        """test88"""
        testcase = """string str = "\n"""
        expect = """string,str,=,Unclosed String: """
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 188))

    def test89(sefl):
        """test89"""
        testcase = """string str = "abc\fabc"""
        expect = """string,str,=,Unclosed String: abc"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 189))
    
    def test90(sefl):
        """test90"""
        testcase = """if (_a_ == 1) return a; """
        expect = """if,(,_a_,==,1,),return,a,;,<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 190))
    
    def test91(sefl):
        """test91"""
        testcase = """float a = 1.3e-1 + 1.4e0 + 1.e-2"""
        expect = """float,a,=,1.3e-1,+,1.4e0,+,1.e-2,<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 191))
    
    def test92(sefl):
        """test92"""
        testcase = """int main() {
                //commnet
                /* 
                */
                printf("Hello world!");
        }"""
        expect = """int,main,(,),{,printf,(,Hello world!,),;,},<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 192))
    
    def test93(sefl):
        """test93"""
        testcase = """int FLOAT = 123;"""
        expect = """int,FLOAT,=,123,;,<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 193))
    
    def test94(sefl):
        """test94"""
        testcase = """do { i-- } while (i > 1)"""
        expect = """do,{,i,-,-,},while,(,i,>,1,),<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 194))
    
    def test95(sefl):
        """test95"""
        testcase = """&&||!-*/"""
        expect = """&&,||,!,-,*,/,<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 195))

    def test96(sefl):
        """test96"""
        testcase = """<==>!=="""
        expect = """<=,=,>,!=,=,<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 196))

    def test97(sefl):
        """test97"""
        testcase = """a/b = 1;"""
        expect = """a,/,b,=,1,;,<EOF>"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 197))
    
    def test98(sefl):
        """test98"""
        testcase = """#include <stdio.h>"""
        expect = """Error Token #"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 198))
    
    def test99(sefl):
        """test99"""
        testcase = """ if (a^b / 2 == 1) return 1;"""
        expect = """if,(,a,Error Token ^"""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 199))
    
    def test100(sefl):
        """test100"""
        testcase = """ "\\\""""
        expect = "Unclosed String: \\\""
        sefl.assertTrue(TestLexer.checkLexeme(testcase, expect, 200))
    
    
