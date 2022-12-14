import knitkit._

class Top extends RawModule {
  val sel = IO(Input(UInt(1.W)))
  val in0 = IO(Input(UInt(1.W)))
  val in1 = IO(Input(UInt(1.W)))
  val out = IO(Output(UInt(1.W)))
  out := (sel & in1) | (~sel & in0)
}

object Main extends App {{
  Driver.execute(() => new Top, args(0))
}}
