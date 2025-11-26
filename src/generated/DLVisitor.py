# Generated from DL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DLParser import DLParser
else:
    from DLParser import DLParser

# This class defines a complete generic visitor for a parse tree produced by DLParser.

class DLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DLParser#program.
    def visitProgram(self, ctx:DLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#StatVarDecl.
    def visitStatVarDecl(self, ctx:DLParser.StatVarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#StatAssign.
    def visitStatAssign(self, ctx:DLParser.StatAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#StatFuncDef.
    def visitStatFuncDef(self, ctx:DLParser.StatFuncDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#StatIf.
    def visitStatIf(self, ctx:DLParser.StatIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#StatWhile.
    def visitStatWhile(self, ctx:DLParser.StatWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#StatFor.
    def visitStatFor(self, ctx:DLParser.StatForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#StatReturn.
    def visitStatReturn(self, ctx:DLParser.StatReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#StatPrint.
    def visitStatPrint(self, ctx:DLParser.StatPrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#StatPlot.
    def visitStatPlot(self, ctx:DLParser.StatPlotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#StatExpr.
    def visitStatExpr(self, ctx:DLParser.StatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#varDeclaration.
    def visitVarDeclaration(self, ctx:DLParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#assignment.
    def visitAssignment(self, ctx:DLParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#functionDef.
    def visitFunctionDef(self, ctx:DLParser.FunctionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#block.
    def visitBlock(self, ctx:DLParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#ifStatement.
    def visitIfStatement(self, ctx:DLParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#whileStatement.
    def visitWhileStatement(self, ctx:DLParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#forStatement.
    def visitForStatement(self, ctx:DLParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#returnStmt.
    def visitReturnStmt(self, ctx:DLParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#printStmt.
    def visitPrintStmt(self, ctx:DLParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#plotStmt.
    def visitPlotStmt(self, ctx:DLParser.PlotStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#ExprMethodCall.
    def visitExprMethodCall(self, ctx:DLParser.ExprMethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#ExprIndex.
    def visitExprIndex(self, ctx:DLParser.ExprIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#ExprAtom.
    def visitExprAtom(self, ctx:DLParser.ExprAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#ExprNot.
    def visitExprNot(self, ctx:DLParser.ExprNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#ExprPower.
    def visitExprPower(self, ctx:DLParser.ExprPowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#ExprRelational.
    def visitExprRelational(self, ctx:DLParser.ExprRelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#ExprAddSub.
    def visitExprAddSub(self, ctx:DLParser.ExprAddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#ExprAnd.
    def visitExprAnd(self, ctx:DLParser.ExprAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#ExprFuncCall.
    def visitExprFuncCall(self, ctx:DLParser.ExprFuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#ExprOr.
    def visitExprOr(self, ctx:DLParser.ExprOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#ExprSlice.
    def visitExprSlice(self, ctx:DLParser.ExprSliceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#ExprMultDiv.
    def visitExprMultDiv(self, ctx:DLParser.ExprMultDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#ExprUnaryMinus.
    def visitExprUnaryMinus(self, ctx:DLParser.ExprUnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#ExprEquality.
    def visitExprEquality(self, ctx:DLParser.ExprEqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#AtomParen.
    def visitAtomParen(self, ctx:DLParser.AtomParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#AtomId.
    def visitAtomId(self, ctx:DLParser.AtomIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#AtomNumber.
    def visitAtomNumber(self, ctx:DLParser.AtomNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#AtomString.
    def visitAtomString(self, ctx:DLParser.AtomStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#AtomBool.
    def visitAtomBool(self, ctx:DLParser.AtomBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#AtomList.
    def visitAtomList(self, ctx:DLParser.AtomListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#AtomNew.
    def visitAtomNew(self, ctx:DLParser.AtomNewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#list.
    def visitList(self, ctx:DLParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#newExpr.
    def visitNewExpr(self, ctx:DLParser.NewExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#number.
    def visitNumber(self, ctx:DLParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DLParser#boolean.
    def visitBoolean(self, ctx:DLParser.BooleanContext):
        return self.visitChildren(ctx)



del DLParser