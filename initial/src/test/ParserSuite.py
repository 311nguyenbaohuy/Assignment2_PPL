import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_declaration0(self):
        input = """
        int main() { }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,200))
    def test_declaration1(self):
        input = """
        int main() { int a; }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    def test_declaration2(self):
        input = """
        int main() { int a }
        """
        expect = "Error on line 2 col 27: }"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_declaration3(self):
        input = """int b;
        int main() { int a; }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_declaration4(self):
        input = """int b;
        void func() {
            b = b + 2;
            return b;
        }
        int main() { int a; }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_declaration5(self):
        input = """int b, c, a[4];
        void func() {
            b = b + 2;
            return b;
        }
        int main() { int a; }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_declaration6(self):
        input = """int b, c, a[];
        void func() {
            b = b + 2;
            return b;
        }
        int main() { int a; }
        """
        expect = "Error on line 1 col 12: ]"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_declaration7(self):
        input = """int;
        void func() {
            b = b + 2;
            return b;
        }
        int main() { int a; }
        """
        expect = "Error on line 1 col 3: ;"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_declaration8(self):
        input = """int b;
        void func(int d,float e, string f) {
            b = b + 2;
            g = g * 2;
            return b;
        }
        int main() { int a; }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_declaration9(self):
        input = """int b = 4.2;
        int main() { int a; }
        """
        expect = "Error on line 1 col 6: ="
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_declaration10(self):
        input = """int b;
        int main() { 
            int foo(int a) {

            }
        }
        """
        expect = "Error on line 3 col 19: ("
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test_declaration11(self):
        input = """int[] b;
        int main() { 
        }
        """
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_declaration12(self):
        input = """int f123;
        int main(int argc, float argv[]) { 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_program0(self):
        input = """for (int 3 = 4; 2 + 5; 4<=2) {}
        int main() { 
        }
        """
        expect = "Error on line 1 col 0: for"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_program1(self):
        input = """x = 4.2 + a[a[5]];
        int main() { 
        }
        void main() {

        }
        """
        expect = "Error on line 1 col 0: x"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_declaration13(self):
        input = """int main(int a, string f);
        void main() {

        }
        """
        expect = "Error on line 1 col 25: ;"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_declaration14(self):
        input = """int main(int a, string f {
        }
        void main() {

        }
        """
        expect = "Error on line 1 col 25: {"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_declaration15(self):
        input = """int main(int a, f) {
        }
        void main() {

        }
        """
        expect = "Error on line 1 col 16: f"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_declaration16(self):
        input = """int main(int a,,f) {
        }
        void main() {

        }
        """
        expect = "Error on line 1 col 15: ,"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_declaration17(self):
        input = """int main(int a, float f,) {
        }
        void main() {

        }
        """
        expect = "Error on line 1 col 24: )"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_declaration18(self):
        input = """int main(int a, float f, void m) {
        }
        void main() {

        }
        """
        expect = "Error on line 1 col 25: void"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    def test_declaration19(self):
        input = """int a, float f;
        void main() {

        }
        """
        expect = "Error on line 1 col 7: float"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_declaration20(self):
        input = """int a, ;
        void main() {

        }
        """
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_statement0(self):
        input = """
        void main() {
            int a;
            if (a = 3) a >= 4;
            else !b[4];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    def test_statement1(self):
        input = """
        void main() {
            int a;
            if (a > 3) {
                a >= 4;
            }

        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_statement2(self):
        input = """
        void main() {
            int a;
            if (a > 3 && a < 5) a = 10;
            else if (a <= 3) a = - a / 2;
            else a = a[2];

        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test_statement3(self):
        input = """
        void main() {
            int a;
            if (a > 3 && a < 5) 
            if (a < 4) a = 10; else a = foo(3, a[5], !4);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_statement4(self):
        input = """
        void main() {
            int a;
            if (a > 3 && a < 5
            if (a < 4) a = 10; else a = foo(3, a[5], !4);
        }
        """
        expect = "Error on line 5 col 12: if"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_statement5(self):
        input = """
        void main() {
            int a;
            if (a * 2 + f[3])
            if (a < 4) a = 10; else a = foo(3, a[5], !4);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_statement6(self):
        input = """
        void main() {
            int a;
            do a+3; if (a * 2 + f[3])
            if (a < 4) a = 10; else a = foo(3, a[5], !4);
            for (i = 2; i < 10; i = i + 1) { }
            while (foo());
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_statement7(self):
        input = """
        void main() {
            int a;
            do
            while (foo());
        }
        """
        expect = "Error on line 5 col 12: while"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_statement8(self):
        input = """
        void main() {
            int a;
            do a + 3;
            while b;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_statement9(self):
        input = """
        void foo() {
            if (a > 3) int a;
        }
        """
        expect = "Error on line 3 col 23: int"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_statement10(self):
        input = """
        void foo() {
            do if (a % 2) a > 3;
            else if (a > 3) b[4];
            else z;
            do a > 3; while (2 * x);
            while (foo()[3]);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    def test_statement11(self):
        input = """
        void foo() {
            for (int i = 2; t / 2; t-1) {

            }
        }
        """
        expect = "Error on line 3 col 17: int"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test_statement12(self):
        input = """
        void foo() {
            int i, j;
            for (i = 2; t / 2; t-1) 
                for (j = 4; j > 10; j = j * j) {

                }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test_statement13(self):
        input = """
        void foo() {
            int i, j; 
            for (i = 2; t / 2; t-1) 
                for (j = 4; j > 10; j = j * j) {
                    break;
                }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_statement14(self):
        input = """
        void foo() {
            int i, j; break; 
            for (i = 2; t / 2; t-1) 
                for (j = 4; j > 10; j = j * j) {
                    break;
                }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test_statement15(self):
        input = """
        void foo() {
            int i, j; continue; 
            for (i = 2; t / 2; t-1) 
                for (j = 4; j > 10; j = j * j) {
                    continue;
                }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test_statement16(self):
        input = """
        void foo() {
            int i, j;
            for (i = 2; t / 2; t-1) 
                for (j = 4; j > 10; j = j * j) {
                    return;
                }
            return x % 2 == 1;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test_statement17(self):
        input = """
        void foo() {
            {
                int a, b, c;
                a=2;
                float f[5];
                if (a == b) f[0] = 1.0;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    def test_expression0(self):
        input = """
        void foo() {
            a = 3 = 4 = 5;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test_expression1(self):
        input = """
        void foo() {
            a = 3 = 4 = 5;
            a = 4 = 3 || 2 = 10 || a;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test_expression2(self):
        input = """
        void foo() {
            a = 3 = 4 = 5;
            a = 4 = 3 || 2 = 10 || a;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test_expression3(self):
        input = """
        void foo() {
            a && 4 = 5;
            a || 2 = 5 && a = 1 || 2;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test_expression4(self):
        input = """
        void foo() {
            a && 4 = 5;
            a || 2 = 5 && a = 1 || 2;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))
    def test_expression5(self):
        input = """
        void foo() {
            a && 4 && 5;
            a || 4 || 5;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    def test_expression6(self):
        input = """
        void foo() {
            a && 4 && 5 == 10;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test_expression7(self):
        input = """
        void foo() {
            a != 4 == 5 != == 3;
        }
        """
        expect = "Error on line 3 col 19: =="
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test_expression8(self):
        input = """
        void foo() {
            a != 4 == 5;
        }
        """
        expect = "Error on line 3 col 19: =="
        self.assertTrue(TestParser.checkParser(input,expect,249))
    def test_expression9(self):
        input = """
        void foo() {
            a < 3;
            4 <= 4 * 2 % 3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))
    def test_expression10(self):
        input = """
        void foo() {
            a < 3 <= 4 * 2 % 3;
        }
        """
        expect = "Error on line 3 col 18: <="
        self.assertTrue(TestParser.checkParser(input,expect,251))
    def test_expression11(self):
        input = """
        void foo() {
            a < 3;
            4 <= 4 + 3 - 4 / 7 * 3 % 2;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    def test_expression12(self):
        input = """
        void foo() {
            a < 3;
            4 <= 4 + 3 - 4 / 7 * 3 % 2;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test_expression13(self):
        input = """
        void foo() {
            a > 3--4;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    def test_expression14(self):
        input = """
        void foo() {
            a > 3------------!4;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    def test_expression15(self):
        input = """
        void foo() {
            a > 3 -- a[2];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test_expression16(self):
        input = """
        void foo() {
            (a+3)[2];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))
    def test_expression17(self):
        input = """
        void foo() {
            (a+3)[foo() + 2];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    def test_expression18(self):
        input = """
        void foo() {
            4[2];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))
    def test_expression19(self):
        input = """
        void foo() {
            bar(2, bar(), a[1/2 == 23])[2];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))
    def test_expression20(self):
        input = """
        void foo() {
            (a[3])[4*10];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    def test_expression21(self):
        input = """
        void foo() {
            (a[3])["123"];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))
    def test_expression22(self):
        input = """
        void foo() {
            (3.5E-2 && "cde" / 2)["123"];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))
    def test_expression23(self):
        input = """
        void foo() {
            arr[arr[arr[foo(2 && arr[1.2E-2])]]];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))
    def test_expression24(self):
        input = """
        void foo() {
            arr[3][2];
        }
        """
        expect = "Error on line 3 col 18: ["
        self.assertTrue(TestParser.checkParser(input,expect,265))
    def test_expression25(self):
        input = """
        void foo() {
            bar((4+2)*2, 3>=4, true);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test_expression26(self):
        input = """
        void foo() {
            bar((4+2)*2, 3>=4, true);
        }
        void f(int arr[10]) { }
        """
        expect = "Error on line 5 col 23: 10"
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test_expression27(self):
        input = """
        void foo() {
            bar((4+2)*2, 3>=4, true);
        }
        void f(int arr[]) { 
            return 1;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test_expression28(self):
        input = """
        void foo() {
            bar((4+2)*2, 3>=4, true);
        }
        void f(int arr[]) { 
            return a[4] * "xde" = 2 || 244.1231;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test_expression29(self):
        input = """
        void foo() {
            bar((4+2)*2, 3>=4, true);
        }
        void f(int arr[]) { 
            return (((((5)))));
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    def test_expression30(self):
        input = """
        void foo() {
            bar((4+2)*2, 3>=4, true);
        }
        void f(int arr[]) { 
            return arr[arr[arr[arr[arr[3]]]]];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_filler0(self):
        input = """
        int f;
        int main(int argc[], string abc[4]) {

        }
        """
        expect = "Error on line 3 col 40: 4"
        self.assertTrue(TestParser.checkParser(input,expect,272))
    def test_filler1(self):
        input = """
        int f;
        int main(int argc[], string abc[]) {
            return foo(foo(foo(foo(foo(0)))));
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))
    def test_filler2(self):
        input = """
        int f;
        main(f[], 3*2, "dadada");
        """
        expect = "Error on line 3 col 8: main"
        self.assertTrue(TestParser.checkParser(input,expect,274))
    def test_filler3(self):
        input = """
        int main() {
            for (;;) {

            }
        }
        """
        expect = "Error on line 3 col 17: ;"
        self.assertTrue(TestParser.checkParser(input,expect,275))
    def test_filler4(self):
        input = """
        int main() {
            do {

            } while do {
                while
            }
        }
        """
        expect = "Error on line 5 col 20: do"
        self.assertTrue(TestParser.checkParser(input,expect,276))
    def test_filler5(self):
        input = """
        int f;
        int main() {
            main(f[], 3*2, "dadada");
        }
        """
        expect = "Error on line 4 col 19: ]"
        self.assertTrue(TestParser.checkParser(input,expect,277))
    def test_filler6(self):
        input = """
        int f;
        int main() {
            do 
            {
                {
                    if (m < 2 || m > 2) return;
                    {
                        {
                            for (a%2; a; a = a > 2) {

                            }
                        }
                    }
                }
                break;
            }
            while func(x*x*x*x);        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))
    def test_filler7(self):
        input = """
        int f;
        int main() {
            float();
        }
        """
        expect = "Error on line 4 col 17: ("
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test_filler8(self):
        input = """
        int f;
        int main() {
            do {

            }
            {
                
            }
            while x > 3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))
    def test_filler9(self):
        input = """
        int f;
        int main() {
            for (i = 0; i < 3; i+1) if (a=b) c=d; else d;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    def test_filler10(self):
        input = """
        int f;
        int main() {
            for (i = 0; i < 3; i+1)
            for (t * t; !z; (((((3))))))
            for (foo(foo(2+arr[3>4]));i;1) {

            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))
    def test_filler12(self):
        input = """
        int f;
        int main() {
            for (i = 0; i < 3; i+1)
            for (t * t; !z; (((((3))))))
            for (foo(foo(2+arr[3>4]));i;1) {
                do do do do do 3+2;
                while 1; while 1; while 1; while 1; while 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))
    def test_filler13(self):
        input = """
        int f;
        int main() {
            f = foo(());
        }

        """
        expect = "Error on line 4 col 21: )"
        self.assertTrue(TestParser.checkParser(input,expect,284))
    def test_filler14(self):
        input = """
        int f;
        void enter()
        {
        }

        void init()
        {
        }

        void print()
        {
        }

        int main()
        {
            enter();
            init();
            print();
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))
    def test_filler15(self):
        input = """
        float f;
        string getString() {
            return "something";
        }

        float[] generate(float a) {
            for (; i > 10; i) {

            }
        }
        """
        expect = "Error on line 8 col 17: ;"
        self.assertTrue(TestParser.checkParser(input,expect,286))
    def test_filler16(self):
        input = """
            int main() {
                /* adasd 
                a = b + c;
                for (a; b; c) {

                }
                do return; while 1;
            } 
        }*/
        """
        expect = "Error on line 11 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,287))
    def test_filler17(self):
        input = """
            int main() {
                /* for (;;;) {

                } */
                a = b + c;
                for (a; b; c) {

                }
                do return; while 1;
            } 
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))
    def test_filler18(self):
        input = """
            int main() {
                a = b + c;
                for (a; b; c) {
                    printf("this is a typical string \\n");
                }
                do return; while 1;
            } 
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))
    def test_filler19(self):
        input = """
            int main() {
                a = b + c;
                for (a; b; c) {
                    printf("this is not a typical string 
                    ");
                }
                do return; while 1;
            } 
        """
        expect = "this is not a typical string "
        self.assertTrue(TestParser.checkParser(input,expect,290))
    def test_filler20(self):
        input = """
            int main(int argc, float argv[3]) {
                
                do return; while 1;
            } 
        """
        expect = "Error on line 2 col 42: 3"
        self.assertTrue(TestParser.checkParser(input,expect,291))
    def test_filler21(self):
        input = """
        """
        expect = "Error on line 2 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    def test_filler22(self):
        input = """
        int main() {
            float f;
            f = 1 > 10 * 2 || 0000.E-00000;
            string v;
            v = 2;
            int t; 
            t = "asdada";
            a = das[31231*a[3232]];
            string a[100];
            a[23=232] = !-("2131" < 10);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))
    def test_filler23(self):
        input = """
        float f;
        f = 12;
        float t;
        """
        expect = "Error on line 3 col 8: f"
        self.assertTrue(TestParser.checkParser(input,expect,294))
    def test_filler24(self):
        input = """
        int main(((((int i;))))) {

        }
        """
        expect = "Error on line 2 col 17: ("
        self.assertTrue(TestParser.checkParser(input,expect,295))
    def test_filler25(self):
        input = """
        void[] foo() {

        }
        """
        expect = "Error on line 2 col 12: ["
        self.assertTrue(TestParser.checkParser(input,expect,296))
    def test_filler26(self):
        input = """
        void foo() {
            do 
            break;
            break;
            break;
            while break;
        }
        """
        expect = "Error on line 7 col 18: break"
        self.assertTrue(TestParser.checkParser(input,expect,297))
    def test_filler27(self):
        input = """
        void foo() {
            do 
            break;
            break;
            break;
            while a > 3;
        }
        int main() {
            foo() = foo();
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))
    def test_filler28(self):
        input = """
        int main() {
            bob(2)[3 + abc + foo(2)[65 + fob(2) * 7 + (14 || 5)]];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect,299))