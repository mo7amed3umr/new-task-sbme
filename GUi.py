from PyQt5.QtWidgets import QOpenGLWidget
# import OpenGL.GL
class GLWidget(QOpenGLWidget):
  def __init__(self, version_profile = None, parent = None):
    super(GLWidget, self).__init__(parent)
    self.version_profile = version_profile

  def initializeGL(self):
    self.gtx = self.QOpenGLContext.currentContext().functions()

    self.gl = self.gtx.context().versionFunctions(self.version_profile)

    self.gl.initializeGLFunctions()

    self.gl.glClearColor(1.0, 0.5, 0.5, 1.0)
    self.gl.glClear(self.gl.GL_COLOR_BUFFER_BIT)

  def paintGL(self):
    pass

  def resizeGL(self, width, height):
    pass