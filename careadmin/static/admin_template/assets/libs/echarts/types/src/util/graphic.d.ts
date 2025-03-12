import * as pathTool from 'zrender/lib/tool/path.js';
import * as matrix from 'zrender/lib/core/matrix.js';
import * as vector from 'zrender/lib/core/vector.js';
import Path from 'zrender/lib/graphic/Path.js';
import Transformable from 'zrender/lib/core/Transformable.js';
import ZRImage from 'zrender/lib/graphic/Image.js';
import Group from 'zrender/lib/graphic/Group.js';
import ZRText from 'zrender/lib/graphic/Text.js';
import Circle from 'zrender/lib/graphic/shape/Circle.js';
import Ellipse from 'zrender/lib/graphic/shape/Ellipse.js';
import Sector from 'zrender/lib/graphic/shape/Sector.js';
import Ring from 'zrender/lib/graphic/shape/Ring.js';
import Polygon from 'zrender/lib/graphic/shape/Polygon.js';
import Polyline from 'zrender/lib/graphic/shape/Polyline.js';
import Rect from 'zrender/lib/graphic/shape/Rect.js';
import Line from 'zrender/lib/graphic/shape/Line.js';
import BezierCurve from 'zrender/lib/graphic/shape/BezierCurve.js';
import Arc from 'zrender/lib/graphic/shape/Arc.js';
import CompoundPath from 'zrender/lib/graphic/CompoundPath.js';
import LinearGradient from 'zrender/lib/graphic/LinearGradient.js';
import RadialGradient from 'zrender/lib/graphic/RadialGradient.js';
import BoundingRect from 'zrender/lib/core/BoundingRect.js';
import OrientedBoundingRect from 'zrender/lib/core/OrientedBoundingRect.js';
import Point from 'zrender/lib/core/Point.js';
import IncrementalDisplayable from 'zrender/lib/graphic/IncrementalDisplayable.js';
import * as subPixelOptimizeUtil from 'zrender/lib/graphic/helper/subPixelOptimize.js';
import { Dictionary } from 'zrender/lib/core/types.js';
import { DisplayableProps } from 'zrender/lib/graphic/Displayable.js';
import Element from 'zrender/lib/Element.js';
import Model from '../model/Model.js';
import { AnimationOptionMixin, ZRRectLike, CommonTooltipOption } from './types.js';
import ComponentModel from '../model/Component.js';
import { updateProps, initProps, removeElement, removeElementWithFadeOut, isElementRemoved } from '../animation/basicTransition.js';
/**
 * @deprecated export for compatitable reason
 */
export { updateProps, initProps, removeElement, removeElementWithFadeOut, isElementRemoved };
declare type ExtendShapeOpt = Parameters<typeof Path.extend>[0];
declare type ExtendShapeReturn = ReturnType<typeof Path.extend>;
/**
 * Extend shape with parameters
 */
export declare function extendShape(opts: ExtendShapeOpt): ExtendShapeReturn;
declare const extendPathFromString: typeof pathTool.extendFromString;
declare type SVGPathOption = Parameters<typeof extendPathFromString>[1];
declare type SVGPathCtor = ReturnType<typeof extendPathFromString>;
declare type SVGPath = InstanceType<SVGPathCtor>;
/**
 * Extend path
 */
export declare function extendPath(pathData: string, opts: SVGPathOption): SVGPathCtor;
/**
 * Register a user defined shape.
 * The shape class can be fetched by `getShapeClass`
 * This method will overwrite the registered shapes, including
 * the registered built-in shapes, if using the same `name`.
 * The shape can be used in `custom series` and
 * `graphic component` by declaring `{type: name}`.
 *
 * @param name
 * @param ShapeClass Can be generated by `extendShape`.
 */
export declare function registerShape(name: string, ShapeClass: {
    new (): Path;
}): void;
/**
 * Find shape class registered by `registerShape`. Usually used in
 * fetching user defined shape.
 *
 * [Caution]:
 * (1) This method **MUST NOT be used inside echarts !!!**, unless it is prepared
 * to use user registered shapes.
 * Because the built-in shape (see `getBuiltInShape`) will be registered by
 * `registerShape` by default. That enables users to get both built-in
 * shapes as well as the shapes belonging to themsleves. But users can overwrite
 * the built-in shapes by using names like 'circle', 'rect' via calling
 * `registerShape`. So the echarts inner featrues should not fetch shapes from here
 * in case that it is overwritten by users, except that some features, like
 * `custom series`, `graphic component`, do it deliberately.
 *
 * (2) In the features like `custom series`, `graphic component`, the user input
 * `{tpye: 'xxx'}` does not only specify shapes but also specify other graphic
 * elements like `'group'`, `'text'`, `'image'` or event `'path'`. Those names
 * are reserved names, that is, if some user registers a shape named `'image'`,
 * the shape will not be used. If we intending to add some more reserved names
 * in feature, that might bring break changes (disable some existing user shape
 * names). But that case probably rarely happens. So we don't make more mechanism
 * to resolve this issue here.
 *
 * @param name
 * @return The shape class. If not found, return nothing.
 */
export declare function getShapeClass(name: string): {
    new (): Path;
};
/**
 * Create a path element from path data string
 * @param pathData
 * @param opts
 * @param rect
 * @param layout 'center' or 'cover' default to be cover
 */
export declare function makePath(pathData: string, opts: SVGPathOption, rect: ZRRectLike, layout?: 'center' | 'cover'): SVGPath;
/**
 * Create a image element from image url
 * @param imageUrl image url
 * @param opts options
 * @param rect constrain rect
 * @param layout 'center' or 'cover'. Default to be 'cover'
 */
export declare function makeImage(imageUrl: string, rect: ZRRectLike, layout?: 'center' | 'cover'): ZRImage;
export declare const mergePath: typeof pathTool.mergePath;
/**
 * Resize a path to fit the rect
 * @param path
 * @param rect
 */
export declare function resizePath(path: SVGPath, rect: ZRRectLike): void;
/**
 * Sub pixel optimize line for canvas
 */
export declare function subPixelOptimizeLine(shape: {
    x1: number;
    y1: number;
    x2: number;
    y2: number;
}, lineWidth: number): {
    x1: number;
    y1: number;
    x2: number;
    y2: number;
};
/**
 * Sub pixel optimize rect for canvas
 */
export declare function subPixelOptimizeRect(param: {
    shape: {
        x: number;
        y: number;
        width: number;
        height: number;
    };
    style: {
        lineWidth: number;
    };
}): {
    shape: {
        x: number;
        y: number;
        width: number;
        height: number;
    };
    style: {
        lineWidth: number;
    };
};
/**
 * Sub pixel optimize for canvas
 *
 * @param position Coordinate, such as x, y
 * @param lineWidth Should be nonnegative integer.
 * @param positiveOrNegative Default false (negative).
 * @return Optimized position.
 */
export declare const subPixelOptimize: typeof subPixelOptimizeUtil.subPixelOptimize;
/**
 * Get transform matrix of target (param target),
 * in coordinate of its ancestor (param ancestor)
 *
 * @param target
 * @param [ancestor]
 */
export declare function getTransform(target: Transformable, ancestor?: Transformable): matrix.MatrixArray;
/**
 * Apply transform to an vertex.
 * @param target [x, y]
 * @param transform Can be:
 *      + Transform matrix: like [1, 0, 0, 1, 0, 0]
 *      + {position, rotation, scale}, the same as `zrender/Transformable`.
 * @param invert Whether use invert matrix.
 * @return [x, y]
 */
export declare function applyTransform(target: vector.VectorArray, transform: Transformable | matrix.MatrixArray, invert?: boolean): number[];
/**
 * @param direction 'left' 'right' 'top' 'bottom'
 * @param transform Transform matrix: like [1, 0, 0, 1, 0, 0]
 * @param invert Whether use invert matrix.
 * @return Transformed direction. 'left' 'right' 'top' 'bottom'
 */
export declare function transformDirection(direction: 'left' | 'right' | 'top' | 'bottom', transform: matrix.MatrixArray, invert?: boolean): 'left' | 'right' | 'top' | 'bottom';
/**
 * Apply group transition animation from g1 to g2.
 * If no animatableModel, no animation.
 */
export declare function groupTransition(g1: Group, g2: Group, animatableModel: Model<AnimationOptionMixin>): void;
export declare function clipPointsByRect(points: vector.VectorArray[], rect: ZRRectLike): number[][];
/**
 * Return a new clipped rect. If rect size are negative, return undefined.
 */
export declare function clipRectByRect(targetRect: ZRRectLike, rect: ZRRectLike): ZRRectLike | undefined;
export declare function createIcon(iconStr: string, // Support 'image://' or 'path://' or direct svg path.
opt?: Omit<DisplayableProps, 'style'>, rect?: ZRRectLike): SVGPath | ZRImage;
/**
 * Return `true` if the given line (line `a`) and the given polygon
 * are intersect.
 * Note that we do not count colinear as intersect here because no
 * requirement for that. We could do that if required in future.
 */
export declare function linePolygonIntersect(a1x: number, a1y: number, a2x: number, a2y: number, points: vector.VectorArray[]): boolean;
/**
 * Return `true` if the given two lines (line `a` and line `b`)
 * are intersect.
 * Note that we do not count colinear as intersect here because no
 * requirement for that. We could do that if required in future.
 */
export declare function lineLineIntersect(a1x: number, a1y: number, a2x: number, a2y: number, b1x: number, b1y: number, b2x: number, b2y: number): boolean;
export declare function setTooltipConfig(opt: {
    el: Element;
    componentModel: ComponentModel;
    itemName: string;
    itemTooltipOption?: string | CommonTooltipOption<unknown>;
    formatterParamsExtra?: Dictionary<unknown>;
}): void;
export declare function traverseElements(els: Element | Element[] | undefined | null, cb: (el: Element) => boolean | void): void;
export { Group, ZRImage as Image, ZRText as Text, Circle, Ellipse, Sector, Ring, Polygon, Polyline, Rect, Line, BezierCurve, Arc, IncrementalDisplayable, CompoundPath, LinearGradient, RadialGradient, BoundingRect, OrientedBoundingRect, Point, Path };
