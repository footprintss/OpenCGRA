"""
==========================================================================
TwoSeqComb.py
==========================================================================
Simple generic two sequentially combined functional units for CGRA tile.

Author : Cheng Tan
  Date : November 28, 2019

"""

from pymtl3 import *
from pymtl3.stdlib.ifcs import SendIfcRTL, RecvIfcRTL
from .opt_type import *

class TwoSeqComb( Component ):

  def construct( s, DataType, Fu0, Fu1 ):

    # Constant
    OptType = Bits5

    # Interface
    s.recv_in0  = RecvIfcRTL( DataType )
    s.recv_in1  = RecvIfcRTL( DataType )
    s.recv_in2  = RecvIfcRTL( DataType )
    s.recv_opt0 = RecvIfcRTL( DataType )
    s.recv_opt1 = RecvIfcRTL( DataType )
    s.send_out  = SendIfcRTL( DataType )

    # Components
    s.Fu0 = Fu0( DataType )
    s.Fu1 = Fu1( DataType )

    # Connections
    s.recv_in0.msg     //= s.Fu0.recv_in0.msg
    s.recv_in1.msg     //= s.Fu0.recv_in1.msg
    s.recv_in2.msg     //= s.Fu1.recv_in1.msg
    s.Fu0.send_out.msg //= s.Fu1.recv_in0.msg
    s.Fu1.send_out.msg //= s.send_out.msg

    @s.update
    def comb_logic():
      s.Fu0.recv_opt.msg = s.recv_opt0.msg
      s.Fu1.recv_opt.msg = s.recv_opt1.msg

    @s.update
    def update_signal():
      s.recv_in0.rdy  = s.send_out.rdy
      s.recv_in1.rdy  = s.send_out.rdy
      s.recv_in2.rdy  = s.send_out.rdy
      s.recv_opt0.rdy = s.send_out.rdy
      s.recv_opt1.rdy = s.send_out.rdy
      s.send_out.en   = s.recv_in0.en  and s.recv_in1.en and s.recv_in2.en and\
                        s.recv_opt0.en and s.recv_opt1.en

  def line_trace( s ):
    return f'[{s.recv_in0.msg}] {OPT_SYMBOL_DICT[s.recv_opt0.msg]} [{s.recv_in1.msg}] {OPT_SYMBOL_DICT[s.recv_opt1.msg]} [{s.recv_in2.msg}] = [{s.send_out.msg}]'
