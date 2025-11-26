# Generated from DL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DLParser import DLParser
else:
    from DLParser import DLParser

# This class defines a complete listener for a parse tree produced by DLParser.
class DLListener(ParseTreeListener):

    # Enter a parse tree produced by DLParser#program.
    def enterProgram(self, ctx:DLParser.ProgramContext):
        pass

    # Exit a parse tree produced by DLParser#program.
    def exitProgram(self, ctx:DLParser.ProgramContext):
        pass


    # Enter a parse tree produced by DLParser#StatVarDecl.
    def enterStatVarDecl(self, ctx:DLParser.StatVarDeclContext):
        pass

    # Exit a parse tree produced by DLParser#StatVarDecl.
    def exitStatVarDecl(self, ctx:DLParser.StatVarDeclContext):
        pass


    # Enter a parse tree produced by DLParser#StatAssign.
    def enterStatAssign(self, ctx:DLParser.StatAssignContext):
        pass

    # Exit a parse tree produced by DLParser#StatAssign.
    def exitStatAssign(self, ctx:DLParser.StatAssignContext):
        pass


    # Enter a parse tree produced by DLParser#StatFuncDef.
    def enterStatFuncDef(self, ctx:DLParser.StatFuncDefContext):
        pass

    # Exit a parse tree produced by DLParser#StatFuncDef.
    def exitStatFuncDef(self, ctx:DLParser.StatFuncDefContext):
        pass


    # Enter a parse tree produced by DLParser#StatIf.
    def enterStatIf(self, ctx:DLParser.StatIfContext):
        pass

    # Exit a parse tree produced by DLParser#StatIf.
    def exitStatIf(self, ctx:DLParser.StatIfContext):
        pass


    # Enter a parse tree produced by DLParser#StatWhile.
    def enterStatWhile(self, ctx:DLParser.StatWhileContext):
        pass

    # Exit a parse tree produced by DLParser#StatWhile.
    def exitStatWhile(self, ctx:DLParser.StatWhileContext):
        pass


    # Enter a parse tree produced by DLParser#StatFor.
    def enterStatFor(self, ctx:DLParser.StatForContext):
        pass

    # Exit a parse tree produced by DLParser#StatFor.
    def exitStatFor(self, ctx:DLParser.StatForContext):
        pass


    # Enter a parse tree produced by DLParser#StatReturn.
    def enterStatReturn(self, ctx:DLParser.StatReturnContext):
        pass

    # Exit a parse tree produced by DLParser#StatReturn.
    def exitStatReturn(self, ctx:DLParser.StatReturnContext):
        pass


    # Enter a parse tree produced by DLParser#StatPrint.
    def enterStatPrint(self, ctx:DLParser.StatPrintContext):
        pass

    # Exit a parse tree produced by DLParser#StatPrint.
    def exitStatPrint(self, ctx:DLParser.StatPrintContext):
        pass


    # Enter a parse tree produced by DLParser#StatPlot.
    def enterStatPlot(self, ctx:DLParser.StatPlotContext):
        pass

    # Exit a parse tree produced by DLParser#StatPlot.
    def exitStatPlot(self, ctx:DLParser.StatPlotContext):
        pass


    # Enter a parse tree produced by DLParser#StatExpr.
    def enterStatExpr(self, ctx:DLParser.StatExprContext):
        pass

    # Exit a parse tree produced by DLParser#StatExpr.
    def exitStatExpr(self, ctx:DLParser.StatExprContext):
        pass


    # Enter a parse tree produced by DLParser#varDeclaration.
    def enterVarDeclaration(self, ctx:DLParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by DLParser#varDeclaration.
    def exitVarDeclaration(self, ctx:DLParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by DLParser#assignment.
    def enterAssignment(self, ctx:DLParser.AssignmentContext):
        pass

    # Exit a parse tree produced by DLParser#assignment.
    def exitAssignment(self, ctx:DLParser.AssignmentContext):
        pass


    # Enter a parse tree produced by DLParser#functionDef.
    def enterFunctionDef(self, ctx:DLParser.FunctionDefContext):
        pass

    # Exit a parse tree produced by DLParser#functionDef.
    def exitFunctionDef(self, ctx:DLParser.FunctionDefContext):
        pass


    # Enter a parse tree produced by DLParser#block.
    def enterBlock(self, ctx:DLParser.BlockContext):
        pass

    # Exit a parse tree produced by DLParser#block.
    def exitBlock(self, ctx:DLParser.BlockContext):
        pass


    # Enter a parse tree produced by DLParser#ifStatement.
    def enterIfStatement(self, ctx:DLParser.IfStatementContext):
        pass

    # Exit a parse tree produced by DLParser#ifStatement.
    def exitIfStatement(self, ctx:DLParser.IfStatementContext):
        pass


    # Enter a parse tree produced by DLParser#whileStatement.
    def enterWhileStatement(self, ctx:DLParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by DLParser#whileStatement.
    def exitWhileStatement(self, ctx:DLParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by DLParser#forStatement.
    def enterForStatement(self, ctx:DLParser.ForStatementContext):
        pass

    # Exit a parse tree produced by DLParser#forStatement.
    def exitForStatement(self, ctx:DLParser.ForStatementContext):
        pass


    # Enter a parse tree produced by DLParser#returnStmt.
    def enterReturnStmt(self, ctx:DLParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by DLParser#returnStmt.
    def exitReturnStmt(self, ctx:DLParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by DLParser#printStmt.
    def enterPrintStmt(self, ctx:DLParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by DLParser#printStmt.
    def exitPrintStmt(self, ctx:DLParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by DLParser#plotStmt.
    def enterPlotStmt(self, ctx:DLParser.PlotStmtContext):
        pass

    # Exit a parse tree produced by DLParser#plotStmt.
    def exitPlotStmt(self, ctx:DLParser.PlotStmtContext):
        pass


    # Enter a parse tree produced by DLParser#ExprMethodCall.
    def enterExprMethodCall(self, ctx:DLParser.ExprMethodCallContext):
        pass

    # Exit a parse tree produced by DLParser#ExprMethodCall.
    def exitExprMethodCall(self, ctx:DLParser.ExprMethodCallContext):
        pass


    # Enter a parse tree produced by DLParser#ExprIndex.
    def enterExprIndex(self, ctx:DLParser.ExprIndexContext):
        pass

    # Exit a parse tree produced by DLParser#ExprIndex.
    def exitExprIndex(self, ctx:DLParser.ExprIndexContext):
        pass


    # Enter a parse tree produced by DLParser#ExprAtom.
    def enterExprAtom(self, ctx:DLParser.ExprAtomContext):
        pass

    # Exit a parse tree produced by DLParser#ExprAtom.
    def exitExprAtom(self, ctx:DLParser.ExprAtomContext):
        pass


    # Enter a parse tree produced by DLParser#ExprNot.
    def enterExprNot(self, ctx:DLParser.ExprNotContext):
        pass

    # Exit a parse tree produced by DLParser#ExprNot.
    def exitExprNot(self, ctx:DLParser.ExprNotContext):
        pass


    # Enter a parse tree produced by DLParser#ExprPower.
    def enterExprPower(self, ctx:DLParser.ExprPowerContext):
        pass

    # Exit a parse tree produced by DLParser#ExprPower.
    def exitExprPower(self, ctx:DLParser.ExprPowerContext):
        pass


    # Enter a parse tree produced by DLParser#ExprRelational.
    def enterExprRelational(self, ctx:DLParser.ExprRelationalContext):
        pass

    # Exit a parse tree produced by DLParser#ExprRelational.
    def exitExprRelational(self, ctx:DLParser.ExprRelationalContext):
        pass


    # Enter a parse tree produced by DLParser#ExprAddSub.
    def enterExprAddSub(self, ctx:DLParser.ExprAddSubContext):
        pass

    # Exit a parse tree produced by DLParser#ExprAddSub.
    def exitExprAddSub(self, ctx:DLParser.ExprAddSubContext):
        pass


    # Enter a parse tree produced by DLParser#ExprAnd.
    def enterExprAnd(self, ctx:DLParser.ExprAndContext):
        pass

    # Exit a parse tree produced by DLParser#ExprAnd.
    def exitExprAnd(self, ctx:DLParser.ExprAndContext):
        pass


    # Enter a parse tree produced by DLParser#ExprFuncCall.
    def enterExprFuncCall(self, ctx:DLParser.ExprFuncCallContext):
        pass

    # Exit a parse tree produced by DLParser#ExprFuncCall.
    def exitExprFuncCall(self, ctx:DLParser.ExprFuncCallContext):
        pass


    # Enter a parse tree produced by DLParser#ExprOr.
    def enterExprOr(self, ctx:DLParser.ExprOrContext):
        pass

    # Exit a parse tree produced by DLParser#ExprOr.
    def exitExprOr(self, ctx:DLParser.ExprOrContext):
        pass


    # Enter a parse tree produced by DLParser#ExprSlice.
    def enterExprSlice(self, ctx:DLParser.ExprSliceContext):
        pass

    # Exit a parse tree produced by DLParser#ExprSlice.
    def exitExprSlice(self, ctx:DLParser.ExprSliceContext):
        pass


    # Enter a parse tree produced by DLParser#ExprMultDiv.
    def enterExprMultDiv(self, ctx:DLParser.ExprMultDivContext):
        pass

    # Exit a parse tree produced by DLParser#ExprMultDiv.
    def exitExprMultDiv(self, ctx:DLParser.ExprMultDivContext):
        pass


    # Enter a parse tree produced by DLParser#ExprUnaryMinus.
    def enterExprUnaryMinus(self, ctx:DLParser.ExprUnaryMinusContext):
        pass

    # Exit a parse tree produced by DLParser#ExprUnaryMinus.
    def exitExprUnaryMinus(self, ctx:DLParser.ExprUnaryMinusContext):
        pass


    # Enter a parse tree produced by DLParser#ExprEquality.
    def enterExprEquality(self, ctx:DLParser.ExprEqualityContext):
        pass

    # Exit a parse tree produced by DLParser#ExprEquality.
    def exitExprEquality(self, ctx:DLParser.ExprEqualityContext):
        pass


    # Enter a parse tree produced by DLParser#AtomParen.
    def enterAtomParen(self, ctx:DLParser.AtomParenContext):
        pass

    # Exit a parse tree produced by DLParser#AtomParen.
    def exitAtomParen(self, ctx:DLParser.AtomParenContext):
        pass


    # Enter a parse tree produced by DLParser#AtomId.
    def enterAtomId(self, ctx:DLParser.AtomIdContext):
        pass

    # Exit a parse tree produced by DLParser#AtomId.
    def exitAtomId(self, ctx:DLParser.AtomIdContext):
        pass


    # Enter a parse tree produced by DLParser#AtomNumber.
    def enterAtomNumber(self, ctx:DLParser.AtomNumberContext):
        pass

    # Exit a parse tree produced by DLParser#AtomNumber.
    def exitAtomNumber(self, ctx:DLParser.AtomNumberContext):
        pass


    # Enter a parse tree produced by DLParser#AtomString.
    def enterAtomString(self, ctx:DLParser.AtomStringContext):
        pass

    # Exit a parse tree produced by DLParser#AtomString.
    def exitAtomString(self, ctx:DLParser.AtomStringContext):
        pass


    # Enter a parse tree produced by DLParser#AtomBool.
    def enterAtomBool(self, ctx:DLParser.AtomBoolContext):
        pass

    # Exit a parse tree produced by DLParser#AtomBool.
    def exitAtomBool(self, ctx:DLParser.AtomBoolContext):
        pass


    # Enter a parse tree produced by DLParser#AtomList.
    def enterAtomList(self, ctx:DLParser.AtomListContext):
        pass

    # Exit a parse tree produced by DLParser#AtomList.
    def exitAtomList(self, ctx:DLParser.AtomListContext):
        pass


    # Enter a parse tree produced by DLParser#AtomNew.
    def enterAtomNew(self, ctx:DLParser.AtomNewContext):
        pass

    # Exit a parse tree produced by DLParser#AtomNew.
    def exitAtomNew(self, ctx:DLParser.AtomNewContext):
        pass


    # Enter a parse tree produced by DLParser#list.
    def enterList(self, ctx:DLParser.ListContext):
        pass

    # Exit a parse tree produced by DLParser#list.
    def exitList(self, ctx:DLParser.ListContext):
        pass


    # Enter a parse tree produced by DLParser#newExpr.
    def enterNewExpr(self, ctx:DLParser.NewExprContext):
        pass

    # Exit a parse tree produced by DLParser#newExpr.
    def exitNewExpr(self, ctx:DLParser.NewExprContext):
        pass


    # Enter a parse tree produced by DLParser#number.
    def enterNumber(self, ctx:DLParser.NumberContext):
        pass

    # Exit a parse tree produced by DLParser#number.
    def exitNumber(self, ctx:DLParser.NumberContext):
        pass


    # Enter a parse tree produced by DLParser#boolean.
    def enterBoolean(self, ctx:DLParser.BooleanContext):
        pass

    # Exit a parse tree produced by DLParser#boolean.
    def exitBoolean(self, ctx:DLParser.BooleanContext):
        pass



del DLParser