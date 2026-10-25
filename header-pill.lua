-- Centered path pill for Yazi 26.9.1.
-- Spacing is measured in terminal rows, not pixels.

local TEXT = "#a4b9c6"
local PILL = "#333335"
local GAP_BELOW = 1

function Root:layout()
  self._chunks = ui.Layout()
    :direction(ui.Layout.VERTICAL)
    :constraints({
      ui.Constraint.Length(1 + GAP_BELOW),
      ui.Constraint.Length(Tabs.height()),
      ui.Constraint.Fill(1),
      ui.Constraint.Length(1),
    })
    :split(self._area)
end

function Header:redraw()
  -- Draw only on the first row; the remaining header row is blank.
  local area = ui.Rect {
    x = self._area.x,
    y = self._area.y,
    w = self._area.w,
    h = math.min(1, self._area.h),
  }

  local right = self:children_redraw(self.RIGHT)
  self._right_width = right:width()

  -- Reserve symmetrical space so the centered pill does not
  -- overlap the right-hand selection/copy counter.
  local available = area.w - 2 * self._right_width
  local elements = {}

  if available >= 5 then
    local path = ya.readable_path(tostring(self._current.cwd))
      .. self:flags()

    path = ui.truncate(path, {
      max = available - 4,
      rtl = true,
    })

    elements[#elements + 1] = ui.Line {
      ui.Span(""):fg(PILL),
      ui.Span(" " .. path .. " "):fg(TEXT):bg(PILL),
      ui.Span(""):fg(PILL),
    }
      :area(area)
      :align(ui.Align.CENTER)
  end

  elements[#elements + 1] = ui.Line(right)
    :area(area)
    :align(ui.Align.RIGHT)

  return elements
end
