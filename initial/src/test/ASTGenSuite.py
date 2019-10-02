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
            if (a > 10)
                a == 1 + 2;
            else
                a(1);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BinaryOp('>',Id('a'),IntLiteral(10)),BinaryOp('==',Id('a'),BinaryOp('+',IntLiteral(1),IntLiteral(2))),CallExpr(Id('a'),[IntLiteral(1)]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))


    def test54(self):
        input = """
        int main(){
            if (a > 10){
                a <= 1 + 2;
            }
            else{
                a(1);
            }
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BinaryOp('>',Id('a'),IntLiteral(10)),Block([BinaryOp('<=',Id('a'),BinaryOp('+',IntLiteral(1),IntLiteral(2)))]),Block([CallExpr(Id('a'),[IntLiteral(1)])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))


    def test55(self):
        input = """
        int main(){
            if (a > 10)
                if (b > 0)
                    if (c > 0)
                        a = 1;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BinaryOp('>',Id('a'),IntLiteral(10)),If(BinaryOp('>',Id('b'),IntLiteral(0)),If(BinaryOp('>',Id('c'),IntLiteral(0)),BinaryOp('=',Id('a'),IntLiteral(1)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test56(self):
        input = """
        void main(int a[]){
            if (a > 10)
                if (b > 0)
                    if (c > 0)
                        a = 1;
                    else
                        a = 1;
                else
                    (a[3]) = 2;
            else
                (a[3])[3] = foo(1) / 2;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[VarDecl('a',ArrayPointerType(IntType()))],VoidType(),Block([If(BinaryOp('>',Id('a'),IntLiteral(10)),If(BinaryOp('>',Id('b'),IntLiteral(0)),If(BinaryOp('>',Id('c'),IntLiteral(0)),BinaryOp('=',Id('a'),IntLiteral(1)),BinaryOp('=',Id('a'),IntLiteral(1))),BinaryOp('=',ArrayCell(Id('a'),IntLiteral('3')),IntLiteral(2))),BinaryOp('=',ArrayCell(ArrayCell(Id('a'),IntLiteral(3)),IntLiteral(3)),BinaryOp('/',CallExpr(Id('foo'),[IntLiteral(1)]),IntLiteral(2))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))


    def test57(self):
        input = """
        void main(int a[]){
            do
                a + 1;
            while(1);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[VarDecl('a',ArrayPointerType(IntType()))],VoidType(),Block([Dowhile([BinaryOp('+',Id('a'),IntLiteral(1))],IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))


    def test58(self):
        input = """
        void main(){
            do{
                a + 1;
            }
            while(1);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([Dowhile([Block([BinaryOp('+',Id('a'),IntLiteral(1))])],IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))


    def test59(self):
        input = """
        void main(){
            do{
            }
            while(1);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([Dowhile([Block([])],IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))


    def test60(self):
        input = """
        void main(){
            do{
                {}
            }
            while(1>2);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([Dowhile([Block([Block([])])],BinaryOp('>',IntLiteral(1),IntLiteral(2)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))


    def test61(self):
        input = """
        void main(){
            for (a; a; a)
                a = 1;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([For(Id('a'),Id('a'),Id('a'),BinaryOp('=',Id('a'),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))


    def test62(self):
        input = """
        void main(){
            for (a; a; a){
                a = 1;
            }
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([For(Id('a'),Id('a'),Id('a'),Block([BinaryOp('=',Id('a'),IntLiteral(1))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))


    def test63(self):
        input = """
        void main(){
            for (i = 10; i > 1.2; --i){
                a = 1;
            }
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([For(BinaryOp('=',Id('i'),IntLiteral(10)),BinaryOp('>',Id('i'),FloatLiteral(1.2)),UnaryOp('-',UnaryOp('-',Id('i'))),Block([BinaryOp('=',Id('a'),IntLiteral(1))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))


    def test64(self):
        input = """
        void main(){
            break;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([Break()]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))


    def test65(self):
        input = """
        void main(){
            for(1;1;1){
                break;
            }
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([For(IntLiteral(1),IntLiteral(1),IntLiteral(1),Block([Break()]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))


    def test66(self):
        input = """
        void main(){
            for(1;1;1)
                break;

        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([For(IntLiteral(1),IntLiteral(1),IntLiteral(1),Break())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))


    def test67(self):
        input = """
        void main(){
            do{
                break;
            }
            while(1);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([Dowhile([Block([Break()])],IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))


    def test68(self):
        input = """
        void main(){
            do{
                continue;
            }
            while(1);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([Dowhile([Block([Continue()])],IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))


    def test69(self):
        input = """
        void main(){
            int a;
            if (a)
                a = 1;
            return a;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),If(Id('a'),BinaryOp('=',Id('a'),IntLiteral(1))),Return(Id('a'))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))


    def test70(self):
        input = """
        void main(){
            int a;
            if (a)
                do{
                    a = 1;
                }
                while(1);
            else
                return a;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),If(Id('a'),Dowhile([Block([BinaryOp('=',Id('a'),IntLiteral(1))])],IntLiteral(1)),Return(Id('a')))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))


    def test71(self):
        input = """
        void main(){
            int a;
            if (a)
                for ( a < 100; (b+1)[2]/3; c (1+2)%3 > 1)
                {
                }
            else
                return a;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),If(Id('a'),For(BinaryOp('<',Id('a'),IntLiteral(100)),BinaryOp('/',ArrayCell(BinaryOp('+',Id('b'),IntLiteral(1)),IntLiteral(2)),IntLiteral(3)),BinaryOp('>',BinaryOp('%',CallExpr(Id('c'),[BinaryOp('+',IntLiteral(1),IntLiteral(2))]),IntLiteral(3)),IntLiteral(1)),Block([])),Return(Id('a')))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))


    def test72(self):
        input = """
        void main(){
            int a;
            for (1;1;1)
                if (1) 1;
                else 1;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),For(IntLiteral(1),IntLiteral(1),IntLiteral(1),If(IntLiteral(1),IntLiteral(1),IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))


    def test73(self):
        input = """
        void main(){
            int a;
            for (1;1;1)
                do{}
                while(1);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),For(IntLiteral(1),IntLiteral(1),IntLiteral(1),Dowhile([Block([])],IntLiteral(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))


    def test74(self):
        input = """
        void main(){
            int a;
            for (1;1;1){
                do{}
                while(1);
                {
                do{}
                while(1);
                }
            }
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),For(IntLiteral(1),IntLiteral(1),IntLiteral(1),Block([Dowhile([Block([])],IntLiteral(1)),Block([Dowhile([Block([])],IntLiteral(1))])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))


    def test75(self):
        input = """
        void main(){
            for (1; 1; 1)
            do 
                do if (a) a;
                while (a);
            while(a);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([For(IntLiteral(1),IntLiteral(1),IntLiteral(1),Dowhile([Dowhile([If(Id('a'),Id('a'))],Id('a'))],Id('a')))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))


    def test76(self):
        input = """
        void main(){
            for (1; 1; 1)
            do 
                do if (a) a;
                while (a);
            while(a);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([For(IntLiteral(1),IntLiteral(1),IntLiteral(1),Dowhile([Dowhile([If(Id('a'),Id('a'))],Id('a'))],Id('a')))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))


    def test77(self):
        input = """
        void main(){
            for (1; 1; 1)
            do 
                break;
            while(a);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([For(IntLiteral(1),IntLiteral(1),IntLiteral(1),Dowhile([Break()],Id('a')))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))


    def test78(self):
        input = """
        void main(){
            for (1; 1; 1)
                for (1; 1; 1)
                    for (1; 1; 1)
                        if (a > 1) a;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([For(IntLiteral(1),IntLiteral(1),IntLiteral(1),For(IntLiteral(1),IntLiteral(1),IntLiteral(1),For(IntLiteral(1),IntLiteral(1),IntLiteral(1),If(BinaryOp('>',Id('a'),IntLiteral(1)),Id('a')))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))


    def test79(self):
        input = """
        void main(){
            int a;
            a = 100/ 2 + 1.3 - 7 % 2 && 4 || true * (false > 3) / (true <= 2);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),BinaryOp('=',Id('a'),BinaryOp('||',BinaryOp('&&',BinaryOp('-',BinaryOp('+',BinaryOp('/',IntLiteral(100),IntLiteral(2)),FloatLiteral(1.3)),BinaryOp('%',IntLiteral(7),IntLiteral(2))),IntLiteral(4)),BinaryOp('/',BinaryOp('*',BooleanLiteral(bool(1)),BinaryOp('>',BooleanLiteral(bool(0)),IntLiteral(3))),BinaryOp('<=',BooleanLiteral(bool(1)),IntLiteral(2)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))


    def test80(self):
        input = """
        void main(){
            int a, b, c[4];
            a = b[2] = (c[4])[3] + a(a[3] * .23)[1];
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),
        Block([
        VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',ArrayType(4,IntType())),
        BinaryOp('=',Id('a'),
        BinaryOp('=',ArrayCell(Id('b'),IntLiteral(2)),BinaryOp('+',ArrayCell(ArrayCell(Id('c'),IntLiteral(4)),IntLiteral(3)),ArrayCell(CallExpr(Id('a'),[BinaryOp('*',ArrayCell(Id('a'),IntLiteral(3)),FloatLiteral(.23))]),IntLiteral(1)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))


    def test81(self):
        input = """
        void main(){
            // comment 
            /* */
            a = "hello world";
            a = 1.e1;
            a = true;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([BinaryOp('=',Id('a'),StringLiteral('hello world')),BinaryOp('=',Id('a'),FloatLiteral(10.0)),BinaryOp('=',Id('a'),BooleanLiteral(bool(1)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))


    def test82(self):
        input = """
        string main(){
            print(abc);
        }
        void foo(){}
        boolean isPrime(int n){return n;}
        """
        expect = str(Program([FuncDecl(Id('main'),[],StringType(),Block([CallExpr(Id('print'),[Id('abc')])])),FuncDecl(Id('foo'),[],VoidType(),Block([])),FuncDecl(Id('isPrime'),[VarDecl('n',IntType())],BoolType(),Block([Return(Id('n'))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))


    def test83(self):
        input = """
        void main(){
            foo(1.2e1, "abc", true);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([CallExpr(Id('foo'),[FloatLiteral(12.0),StringLiteral('abc'),BooleanLiteral(bool(1))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))


    def test84(self):
        input = """
        void main(){
            if (foo("true")){
                print(foo("true"));
            }
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([If(CallExpr(Id('foo'),[StringLiteral('true')]),Block([CallExpr(Id('print'),[CallExpr(Id('foo'),[StringLiteral('true')])])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))


    def test85(self):
        input = """
        void main(){
            for (foo(1); foo(a[2]) == 1; foo(2) >= 1)
                continue;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([For(CallExpr(Id('foo'),[IntLiteral(1)]),BinaryOp('==',CallExpr(Id('foo'),[ArrayCell(Id('a'),IntLiteral(2))]),IntLiteral(1)),BinaryOp('>=',CallExpr(Id('foo'),[IntLiteral(2)]),IntLiteral(1)),Continue())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))


    def test85(self):
        input = """
        void main(){
            for (foo(1); foo(a[2]) == 1; foo(2) >= 1)
                continue;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([For(CallExpr(Id('foo'),[IntLiteral(1)]),BinaryOp('==',CallExpr(Id('foo'),[ArrayCell(Id('a'),IntLiteral(2))]),IntLiteral(1)),BinaryOp('>=',CallExpr(Id('foo'),[IntLiteral(2)]),IntLiteral(1)),Continue())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))


    def test86(self):
        input = """
        void main(){
            (((1 > 2) <= 3) >= 4) < 5 == 5
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([BinaryOp('==',BinaryOp('<',BinaryOp('>=',BinaryOp('<=',BinaryOp('>',IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),IntLiteral(5)),IntLiteral(5))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))


    def test86(self):
        input = """
        void main(){
            (((1 > 2) <= 3) >= 4) < 5 == 5;
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([BinaryOp('==',BinaryOp('<',BinaryOp('>=',BinaryOp('<=',BinaryOp('>',IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(4)),IntLiteral(5)),IntLiteral(5))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))


    def test87(self):
        input = """
        void main(){
        }
        int[] main(int a[]){
            int a[1];
            print(a[2]);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([])),FuncDecl(Id('main'),[VarDecl('a',ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([VarDecl('a',ArrayType(1,IntType())),CallExpr(Id('print'),[ArrayCell(Id('a'),IntLiteral(2))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))


    def test88(self):
        input = """
        void main(){
        }
        int[] main(int a[]){
        }
        float[] main(string a){}
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([])),FuncDecl(Id('main'),[VarDecl('a',ArrayPointerType(IntType()))],ArrayPointerType(IntType()),Block([])),FuncDecl(Id('main'),[VarDecl('a',StringType())],ArrayPointerType(FloatType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))


    def test89(self):
        input = """
        void main(){
            do{{}{{}}{}{{}}}
            while(1);
        }
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([Dowhile([Block([Block([]),Block([Block([])]),Block([]),Block([Block([])])])],IntLiteral(1))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))


    def test90(self):
        input = """
        void main(){
        }
        int a[1];
        string b[1];
        """
        expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([])),VarDecl('a',ArrayType(1, IntType())),VarDecl('b',ArrayType(1,StringType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))


    def test91(self):
        input = """
        int a;
        string a(){
            int a, b, c;
            if (a % b == c % d){
                print (a + b + c + d);
            }
        }
        """
        expect = str(Program([VarDecl('a',IntType()),FuncDecl(Id('a'),[],StringType(),Block([VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',IntType()),If(BinaryOp('==',BinaryOp('%',Id('a'),Id('b')),BinaryOp('%',Id('c'),Id('d'))),Block([CallExpr(Id('print'),[BinaryOp('+',BinaryOp('+',BinaryOp('+',Id('a'),Id('b')),Id('c')),Id('d'))])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))


    def test92(self):
        input = """
        int a;
        string a(){
            int a, b, c;
            if (a % b == 1){
                print (a);
            }
            else 
                print(b);
        }
        """
        expect = str(Program([VarDecl('a',IntType()),FuncDecl(Id('a'),[],StringType(),Block([VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',IntType()),If(BinaryOp('==',BinaryOp('%',Id('a'),Id('b')),IntLiteral(1)),Block([CallExpr(Id('print'),[Id('a')])]),CallExpr(Id('print'),[Id('b')]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))


    def test93(self):
        input = """
        int gcd (int a, int b){
            if (b == 0) return a;
            gcd (b, a%b);
        }
        """
        expect = str(Program([FuncDecl(Id('gcd'),[VarDecl('a',IntType()),VarDecl('b',IntType())],IntType(),Block([If(BinaryOp('==',Id('b'),IntLiteral(0)),Return(Id('a'))),CallExpr(Id('gcd'),[Id('b'),BinaryOp('%',Id('a'),Id('b'))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))


    def test94(self):
        input = """
        void foo(int n, int arr[]){
            if (n == 0) return;
            print(arr[n]);
            foo(n - 1, arr);
        }
        """
        expect = str(Program([FuncDecl(Id('foo'),[VarDecl('n',IntType()),VarDecl('arr',ArrayPointerType(IntType()))],VoidType(),Block([If(BinaryOp('==',Id('n'),IntLiteral(0)),Return()),CallExpr(Id('print'),[ArrayCell(Id('arr'),Id('n'))]),CallExpr(Id('foo'),[BinaryOp('-',Id('n'),IntLiteral(1)),Id('arr')])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))


    def test95(self):
        input = """
        void foo(){
            if (0) return;
        }
        """
        expect = str(Program([FuncDecl(Id('foo'),[],VoidType(),Block([If(IntLiteral(0),Return())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))


    def test96(self):
        input = """
        void foo(){
            if (0) return;
        }
        """
        expect = str(Program([FuncDecl(Id('foo'),[],VoidType(),Block([If(IntLiteral(0),Return())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))


    def test97(self):
        input = """
        void foo(){
            if (0) continue;
        }
        """
        expect = str(Program([FuncDecl(Id('foo'),[],VoidType(),Block([If(IntLiteral(0),Continue())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))


    def test98(self):
        input = """
        void foo(){
            if (0) break;
        }
        """
        expect = str(Program([FuncDecl(Id('foo'),[],VoidType(),Block([If(IntLiteral(0),Break())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))


    def test99(self):
        input = """
        void foo(){
            if (0) {
                break;
                continue;
                return;
            }
        }
        """
        expect = str(Program([FuncDecl(Id('foo'),[],VoidType(),Block([If(IntLiteral(0),Block([Break(),Continue(),Return()]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))

