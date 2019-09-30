import unittest
from TestUtils import TestAST
from AST import *
# from .TestUtils import TestAST
# from main.mc.utils.AST import *

class ASTGenSuite(unittest.TestCase):
    def test0(self):
        input = """int main, a;"""
        expect = str(Program([VarDecl('main', IntType()), VarDecl('a', IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

 
    def test1(self):
        input = """int main, a[0];"""
        expect = str(Program([VarDecl('main',IntType()), VarDecl('a' ,ArrayType(0, IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))


    def test2(self):
        input = """int main[1], a[0];"""
        expect = str(Program([VarDecl('main',ArrayType(1, IntType())), VarDecl('a' ,ArrayType(0, IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))


    def test3(self):
        input = """float main[1], a[0];"""
        expect = str(Program([VarDecl('main',ArrayType(1, FloatType())), VarDecl('a' ,ArrayType(0, FloatType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))


    def test4(self):
        input = """float _a, a[10];"""
        expect = str(Program([VarDecl('_a', FloatType()), VarDecl('a' ,ArrayType(10, FloatType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))


    def test5(self):
        input = """boolean a, a[0];"""
        expect = str(Program([VarDecl('a', BoolType()), VarDecl('a' ,ArrayType(0, BoolType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))


    def test6(self):
        input = """boolean a[10], a[0];"""
        expect = str(Program([VarDecl('a', ArrayType(10, BoolType())), VarDecl('a' ,ArrayType(0, BoolType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))


    def test7(self):
        input = """
        int a, a[0];
        string b, b[10];
        """
        expect = str(Program([VarDecl('a', IntType()), 
                            VarDecl('a' ,ArrayType(0, IntType())),
                            VarDecl('b', StringType()), 
                            VarDecl('b' ,ArrayType(10, StringType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))


    def test8(self):
        input = """
        float a, a[0];
        string b, b[10];
        """
        expect = str(Program([VarDecl('a', FloatType()), 
                            VarDecl('a' ,ArrayType(0, FloatType())),
                            VarDecl('b', StringType()), 
                            VarDecl('b' ,ArrayType(10, StringType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))


    def test9(self):
        input = """
        float a, a[0];
        string b, b[10];
        boolean c[10], c[10];
        """
        expect = str(Program([VarDecl('a', FloatType()), 
                            VarDecl('a' ,ArrayType(0, FloatType())),
                            VarDecl('b', StringType()), 
                            VarDecl('b' ,ArrayType(10, StringType())),
                            VarDecl('c' ,ArrayType(10, BoolType())),
                            VarDecl('c' ,ArrayType(10, BoolType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))


    def test10(self):
        input = """
        int a, b, c, d;
        float a, a[0];
        string b, b[10];
        boolean c[10], c[10];
        """
        expect = str(Program([VarDecl('a', IntType()),
                            VarDecl('b', IntType()),
                            VarDecl('c', IntType()),
                            VarDecl('d', IntType()),
                            VarDecl('a', FloatType()), 
                            VarDecl('a' ,ArrayType(0, FloatType())),
                            VarDecl('b', StringType()), 
                            VarDecl('b' ,ArrayType(10, StringType())),
                            VarDecl('c' ,ArrayType(10, BoolType())),
                            VarDecl('c' ,ArrayType(10, BoolType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))


    def test11(self):
        input = """
        int main(){

        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))


    def test12(self):
        input = """
        float main(){

        }
        """
        expect = str(Program([FuncDecl(Id('main'),[], FloatType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))


    def test13(self):
        input = """
        string main(){

        }
        """
        expect = str(Program([FuncDecl(Id('main'),[], StringType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))


    def test14(self):
        input = """
        boolean main(){

        }
        """
        expect = str(Program([FuncDecl(Id('main'),[], BoolType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))


    def test15(self):
        input = """
        void main(){

        }
        """
        expect = str(Program([FuncDecl(Id('main'),[], VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))


    def test16(self):
        input = """
        int[] main(){

        }
        """
        expect = str(Program([FuncDecl(Id('main'), [], ArrayPointerType(IntType()), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test17(self):
        input = """
        boolean[] main(){

        }
        """
        expect = str(Program([FuncDecl(Id('main'), [], ArrayPointerType(BoolType()), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test18(self):
        input = """
        float[] main(){
        
        }
        string[] main(){
    
        }
        """
        expect = str(Program([FuncDecl(Id('main'), [], ArrayPointerType(FloatType()), Block([])),
                              FuncDecl(Id('main'), [], ArrayPointerType(StringType()), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))


    def test19(self):
        input = """
        int a, b, c;
        float[] main(){
        
        }
        string[] main(){
    
        }
        string d, e, f;
        """
        expect = str(Program([VarDecl('a', IntType()),
                            VarDecl('b', IntType()),
                            VarDecl('c', IntType()),
                            FuncDecl(Id('main'), [], ArrayPointerType(FloatType()), Block([])),
                            FuncDecl(Id('main'), [], ArrayPointerType(StringType()), Block([])),
                            VarDecl('d', StringType()),
                            VarDecl('e', StringType()),
                            VarDecl('f', StringType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))


    def test20(self):
        input = """
        int main(int a){

        }
        """
        expect = str(Program([FuncDecl(Id('main'), [VarDecl('a', IntType())], IntType(), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))


    def test21(self):
        input = """
        int main(int a, int a[]){

        }
        """
        expect = str(Program([FuncDecl(Id('main'), [VarDecl('a', IntType()), VarDecl('a',ArrayPointerType(IntType()))], IntType(), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test22(self):
        input = """
        int main(boolean a, int a[]){

        }
        """
        expect = str(Program([FuncDecl(Id('main'), [VarDecl('a', BoolType()), VarDecl('a',ArrayPointerType(IntType()))], IntType(), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test23(self):
        input = """
        int main(boolean a, int a[], string a[]){

        }
        """
        expect = str(Program([FuncDecl(Id('main'), [VarDecl('a', BoolType()), VarDecl('a',ArrayPointerType(IntType())), VarDecl('a',ArrayPointerType(StringType()))], IntType(), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test24(self):
        input = """
        void main(float a[], string a[]){

        }
        """
        expect = str(Program([FuncDecl(Id('main'), [VarDecl('a', ArrayPointerType(FloatType())), VarDecl('a',ArrayPointerType(StringType()))], VoidType(), Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test25(self):
        input = """
        int main(){
            int a;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a', IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    
    def test26(self):
        input = """
        int main(){
            int a;
            {}
            {int a;}
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a', IntType()), Block([]), Block([VarDecl('a', IntType())])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))


    def test27(self):
        input = """
        int main(){
            int a;{
            boolean a[5];
            }
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),Block([VarDecl('a',ArrayType(5, BoolType()))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    

    def test28(self):
        input = """
        int main(){
            {
                int a;
            }
            {
                boolean a[5];
            }
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Block([VarDecl('a',IntType())]),Block([VarDecl('a',ArrayType(5, BoolType()))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    

    def test29(self):
        input = """
        int main(){
            int a;
            a = 5;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),BinaryOp('=',Id('a'),IntLiteral(5))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))


    def test30(self):
        input = """
        int main(){
            int a;
            a = b || 1;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),BinaryOp('=',Id('a'),BinaryOp('||',Id('b'),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test31(self):
        input = """
        int main(){
            a = b || c || d;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('||',BinaryOp('||',Id('b'),Id('c')),Id('d')))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))


    def test32(self):
        input = """
        int main(){
            a = b && c || d;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('||',BinaryOp('&&',Id('b'),Id('c')),Id('d')))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))


    def test33(self):
        input = """
        int main(){
            a = b && c && d;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('&&',BinaryOp('&&',Id('b'),Id('c')),Id('d')))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))


    def test34(self):
        input = """
        int main(){
            a = b - c - d + a;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('+',BinaryOp('-',BinaryOp('-',Id('b'),Id('c')),Id('d')),Id('a')))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))


    def test35(self):
        input = """
        int main(){
            a = b / c / d * a * b % c;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('%',BinaryOp('*',BinaryOp('*',BinaryOp('/',BinaryOp('/',Id('b'),Id('c')),Id('d')),Id('a')),Id('b')),Id('c')))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335))


    def test36(self):
        input = """
        int main(){
            a = b / c / d * a * b % c;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('%',BinaryOp('*',BinaryOp('*',BinaryOp('/',BinaryOp('/',Id('b'),Id('c')),Id('d')),Id('a')),Id('b')),Id('c')))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))


    def test37(self):
        input = """
        int main(){
            a = b + c / d - a * b % c + d;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('+',BinaryOp('-',BinaryOp('+',Id('b'),BinaryOp('/',Id('c'),Id('d'))),BinaryOp('%',BinaryOp('*',Id('a'),Id('b')),Id('c'))),Id('d')))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))


    def test37(self):
        input = """
        int main(){
            a = b + c / d - a * b % c + d;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('+',BinaryOp('-',BinaryOp('+',Id('b'),BinaryOp('/',Id('c'),Id('d'))),BinaryOp('%',BinaryOp('*',Id('a'),Id('b')),Id('c'))),Id('d')))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))


    def test38(self):
        input = """
        int main(){
            a = 1.2e2;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),FloatLiteral(120.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))


    def test39(self):
        input = """
        int main(){
            a = .1e2;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),FloatLiteral(10.0))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))


    def test40(self):
        input = """
        int main(){
            a = .1e-2;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),FloatLiteral(0.001))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))


    def test41(self):
        input = """
        int main(){
            a = "abc";
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),StringLiteral('abc'))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))


    def test41(self):
        input = """
        int main(){
            a = "abc";
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),StringLiteral('abc'))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))


    def test42(self):
        input = """
        int main(){
            a = true;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BooleanLiteral(bool(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))


    def test43(self):
        input = """
        int main(){
            a = true || false;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('||',BooleanLiteral(bool(1)),BooleanLiteral(bool(0))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    
    def test44(self):
        input = """
        int main(){
            a = !true;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),UnaryOp('!',BooleanLiteral(bool(1))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
        

    def test45(self):
        input = """
        int main(){
            a = -!true || false;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('||',UnaryOp('-',UnaryOp('!',BooleanLiteral(bool(1)))),BooleanLiteral(bool(0))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
        

    def test46(self):
        input = """
        int main(){
            a = a(0);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),CallExpr(Id('a'),[IntLiteral(0)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test47(self):
        input = """
        int main(){
            a(0, a) = a(a(a));
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',CallExpr(Id('a'),[IntLiteral(0),Id('a')]),CallExpr(Id('a'),[CallExpr(Id('a'),[Id('a')])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))


    def test48(self):
        input = """
        int main(){
            a = (a(1) + 1) / 2;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('/',BinaryOp('+',CallExpr(Id('a'),[IntLiteral(1)]),IntLiteral(1)),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))


    def test49(self):
        input = """
        int main(){
            a = (a(1) + 1) / 2;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('/',BinaryOp('+',CallExpr(Id('a'),[IntLiteral(1)]),IntLiteral(1)),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))


    def test50(self):
        input = """
        int main(){
            a[1] = (a(1) + 1) / 2;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',ArrayCell(Id('a'),IntLiteral(1)),BinaryOp('/',BinaryOp('+',CallExpr(Id('a'),[IntLiteral(1)]),IntLiteral(1)),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))


    def test51(self):
        input = """
        int main(){
            if (a) a = 1;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(Id('a'),BinaryOp('=',Id('a'),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))


    def test52(self):
        input = """
        int main(){
            {
                if (a) a = 1;
            }
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Block([If(Id('a'),BinaryOp('=',Id('a'),IntLiteral(1)))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))


    def test53(self):
        input = """
        int main(){
            do
                a = 1;
            while(a);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([BinaryOp('=',Id('a'),IntLiteral(1))],Id('a'))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))


    def test54(self):
        input = """
        int main(){
            for (a;a;a)
                a = 1;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([BinaryOp('=',Id('a'),IntLiteral(1))],Id('a'))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

